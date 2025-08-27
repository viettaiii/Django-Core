import django_tables2 as tables
from .models import Book

class BookTable(tables.Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap5.html"
        fields = ("title", "author__name", "publication_date", "genre", "price")
        attrs = {"class": "table table-striped table-hover", "id": "bookTable"}

    price = tables.Column(verbose_name="Price ($)")
    def render_price(self, value):
        return f"${value:.2f}"