from django.urls import path
from .views import UserPage

app_name = 'users'

urlpatterns = [
    path('', UserPage.as_view(), name='list'),
]
