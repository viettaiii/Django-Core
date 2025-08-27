import django_filters
from django import forms
from .models import Book, Author
from .forms import BookFilterFormHelper
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Title contains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search title...'})
    )
    author = django_filters.ModelChoiceFilter(
        queryset=Author.objects.all(),
        label='Author',
        widget=forms.Select(attrs={'class': 'form-select select2'})
    )
    genre = django_filters.ChoiceFilter(
        choices=Book.genre.field.choices,
        label='Genre',
        widget=forms.Select(attrs={'class': 'form-select select2'})
    )
    publication_date = django_filters.DateFromToRangeFilter(
        label='Publication Date Range',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    price = django_filters.RangeFilter(
        label='Price Range',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = BookFilterFormHelper()  # Crispy forms để layout ngang