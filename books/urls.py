from django.urls import path
from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('edit/<int:pk>/', lambda request, pk: None, name='book_edit'),  # Placeholder
    path('delete/<int:pk>/', lambda request, pk: None, name='book_delete'),  # Placeholder
]