from core.views import CoreTablePage
from .models import Product, Category

class ProductPage(CoreTablePage):
    model = Product
    page_title = "Products"
    page_actions = [
        {"label": "Add Product", "href": "/admin/products/product/add/"},
        {"label": "Manage Categories", "href": "/admin/products/category/"}
    ]
    
    columns = [
        {"field": "id", "label": "ID", "orderable": True},
        {"field": "name", "label": "Product Name", "linkify": True},
        {"field": "category", "label": "Category"},
        {"field": "price", "label": "Price", "type": "number"},
        {"field": "stock_status", "label": "Stock Status"},
        {"field": "is_active", "label": "Active", "type": "boolean"},
        {"field": "created_at", "label": "Created", "type": "datetime", "format": "M d, Y"},
    ]
    
    filters = {
        "name": {"lookup": "icontains", "type": "text"},
        "category": {"type": "choice", "choices": lambda: [(c.id, c.name) for c in Category.objects.all()]},
        "stock_status": {"type": "choice", "choices": Product.STOCK_CHOICES},
        "is_active": {"type": "boolean"},
        "price_min": {"type": "number", "lookup": "gte", "field": "price"},
        "price_max": {"type": "number", "lookup": "lte", "field": "price"},
        "created_after": {"type": "date", "lookup": "gte", "field": "created_at"},
    }
    
    def get_queryset(self):
        # Optimize with select_related to avoid N+1 queries
        return super().get_queryset().select_related('category', 'created_by')

class CategoryPage(CoreTablePage):
    model = Category
    page_title = "Categories"
    page_actions = [{"label": "Add Category", "href": "/admin/products/category/add/"}]
    
    columns = [
        {"field": "id", "label": "ID", "orderable": True},
        {"field": "name", "label": "Category Name", "linkify": True},
        {"field": "description", "label": "Description"},
        {"field": "created_at", "label": "Created", "type": "datetime", "format": "M d, Y"},
    ]
    
    filters = {
        "name": {"lookup": "icontains", "type": "text"},
        "created_after": {"type": "date", "lookup": "gte", "field": "created_at"},
    }
