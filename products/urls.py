from django.urls import path
from .views import ProductPage, CategoryPage

app_name = 'products'

urlpatterns = [
    path('', ProductPage.as_view(), name='list'),
    path('categories/', CategoryPage.as_view(), name='categories'),
]
