import django_filters
from django import forms  # Explicit import for widgets
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), label='Author', widget=forms.Select(attrs={'class': 'select2'}))
    genre = django_filters.ChoiceFilter(choices=Book.genre.field.choices, label='Genre', widget=forms.Select(attrs={'class': 'select2'}))
    publication_date = django_filters.DateFromToRangeFilter(label='Publication Date Range')
    price = django_filters.RangeFilter(label='Price Range')

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'price']