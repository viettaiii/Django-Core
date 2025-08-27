import random
import django_tables2 as tables
from django.utils.html import format_html
from .models import Book

class BookTable(tables.Table):
    progress = tables.Column(verbose_name='Progress (%)', accessor='pk')  # Giả lập
    status = tables.Column(verbose_name='Status')
    test = tables.Column(verbose_name='Test')
    actions = tables.TemplateColumn(
        template_code='''
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown button
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
        </div>
        ''',
        verbose_name='Actions',
        orderable=False
    )

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap5.html"
        fields = ("title", "author__name", "publication_date", "genre", "price", "progress", "status", "actions")
        attrs = {"class": "table table-striped table-hover", "id": "bookTable"}

    price = tables.Column(verbose_name="Price ($)")
    def render_price(self, value):
        return f"${value:.2f}"
    def render_test(self):
        return f"test"


    def render_progress(self, record):
        progress = random.randint(0, 100)  # Giả lập progress
        return format_html(
            '<div class="progress"><div class="progress-bar bg-success" style="width: {}%">{}</div></div>',
            progress, f"{progress}%"
        )

    def render_status(self, value):
        if value == 'available':
            return format_html('<span class="badge bg-success">{}</span>', value)
        elif value == 'out_of_stock':
            return format_html('<span class="badge bg-warning">{}</span>', value)
        else:
            return format_html('<span class="badge bg-danger">{}</span>', value)