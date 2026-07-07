from django.urls import path
from .views import book_list, book_detail, BookListView, book_share

app_name = 'catalog'

urlpatterns = [
    # path('', book_list, name='book_list'),
    path('', BookListView.as_view(), name='book_list'),
    path('<slug:book>/', book_detail, name='book_detail'),
    path('<slug:book>/share/', book_share, name='book_share'),
]
