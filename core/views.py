from typing import Dict, List, Any
from django.db.models import Model
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
import django_tables2 as tables
import django_filters


# ---- Dynamic Table Class Builder --------------------------------------------

def make_table_class(_model: type[Model], columns: List[Dict[str, Any]]) -> type[tables.Table]:
    """
    Dynamically create a Table class from column configuration.
    
    Args:
        model: Django model class
        columns: List of column configs like:
            [
                {"field": "id", "label": "ID", "orderable": True},
                {"field": "name", "label": "Name", "linkify": True},
                {"field": "created", "label": "Created", "type": "datetime", "format": "Y-m-d"},
            ]
    """
    attrs: Dict[str, Any] = {}
    
    for col in columns:
        field_name = col["field"]
        column_type = col.get("type", "text")
        
        # Choose column class based on type
        if column_type == "boolean":
            ColumnCls = tables.BooleanColumn
        elif column_type == "datetime":
            ColumnCls = tables.DateTimeColumn
        elif column_type == "date":
            ColumnCls = tables.DateColumn
        elif column_type == "number":
            ColumnCls = tables.Column
        else:
            ColumnCls = tables.Column
        
        # Build column kwargs
        kwargs: Dict[str, Any] = {}
        if label := col.get("label"):
            kwargs["verbose_name"] = label
        if "orderable" in col:
            kwargs["orderable"] = col["orderable"]
        if col.get("linkify"):
            kwargs["linkify"] = True
        if fmt := col.get("format"):
            kwargs["format"] = fmt
        
        attrs[field_name] = ColumnCls(**kwargs)
    
    # Meta class for the table
    class Meta:
        model = _model
        template_name = "django_tables2/bootstrap5.html"
        attrs = {"class": "table table-striped table-hover"}
    
    attrs['Meta'] = Meta
    return type('DynamicTable', (tables.Table,), attrs)


# ---- Dynamic FilterSet Class Builder ----------------------------------------

_FILTER_TYPE_MAP = {
    "text": django_filters.CharFilter,
    "number": django_filters.NumberFilter,
    "date": django_filters.DateFilter,
    "datetime": django_filters.DateTimeFilter,
    "boolean": django_filters.BooleanFilter,
    "choice": django_filters.ChoiceFilter,
}

def make_filterset_class(_model: type[Model], filters: Dict[str, Dict[str, Any]]) -> type[django_filters.FilterSet]:
    """
    Dynamically create a FilterSet class from filter configuration.
    
    Args:
        model: Django model class
        filters: Dict of filter configs like:
            {
                "username": {"lookup": "icontains", "type": "text"},
                "is_active": {"type": "boolean"},
                "created_after": {"type": "date", "lookup": "gte", "field": "created_at"},
            }
    """
    attrs: Dict[str, Any] = {}
    
    for name, conf in (filters or {}).items():
        ftype = conf.get("type", "text")
        FilterCls = _FILTER_TYPE_MAP.get(ftype, django_filters.CharFilter)
        kwargs: Dict[str, Any] = {}
        if lookup := conf.get("lookup"):
            kwargs["lookup_expr"] = lookup
        if ftype == "choice" and (choices := conf.get("choices")):
            kwargs["choices"] = choices
        field_name = conf.get("field", name)
        attrs[name] = FilterCls(field_name=field_name, **kwargs)
    
    class Meta:
        model = _model
        fields = list(filters.keys()) if filters else []
    
    attrs['Meta'] = Meta
    return type('DynamicFilterSet', (django_filters.FilterSet,), attrs)


# ---- Core View ---------------------------------------------------------------

class CoreTablePage(SingleTableMixin, FilterView):
    """Base reusable page: renders filters + table with minimal declaration.
    
    Usage:
        class UserPage(CoreTablePage):
            model = get_user_model()
            columns = [ {"field":"id","label":"ID"}, ... ]
            filters = { "username": {"lookup":"icontains"}, ... }
    """
    
    # Required in subclass
    model: type[Model] = None  # Django model
    columns: List[Dict[str, Any]] = []  # column config (see make_table_class)
    
    # Optional: advanced filters config
    filters: Dict[str, Dict[str, Any]] | None = None
    
    # django-tables2 + FilterView defaults
    table_class = None
    filterset_class = None
    template_name = 'core/table_page.html'
    paginate_by = 25
    
    def get_table_class(self):
        if self.table_class:
            return self.table_class
        # Build on-the-fly from config
        return make_table_class(self.model, self.columns)
    
    def get_filterset_class(self):
        if self.filterset_class:
            return self.filterset_class
        if self.filters:
            return make_filterset_class(self.model, self.filters)
        return super().get_filterset_class()
    
    # Supply base queryset; override if you need joins/prefetch
    def get_queryset(self):
        return self.model._default_manager.all()
    
    # Improve context
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.setdefault('page_title', getattr(self, 'page_title', self.model._meta.verbose_name_plural.title()))
        ctx.setdefault('page_actions', getattr(self, 'page_actions', []))  # e.g. [{"label":"Create","href":"/users/new"}]
        return ctx
