from django.views.generic import ListView
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import Book
from .tables import BookTable
from .filters import BookFilter

class BookListView(SingleTableMixin, FilterView, ListView):
    model = Book
    table_class = BookTable
    filterset_class = BookFilter
    template_name = 'books/book_list.html'
    paginate_by = 10  # Server-side pagination (có thể tắt nếu dùng DataTables client-side)

    def get_queryset(self):
        return super().get_queryset().select_related('author')  # Join Author