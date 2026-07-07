from django.urls import path
from .views import book_list, book_detail

app_name = 'catalog'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('<slug:book>/', book_detail, name='book_detail')
]
