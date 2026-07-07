from django.urls import path
from .views import book_list, book_detail, BookListView, book_share, book_review

app_name = 'catalog'

urlpatterns = [
    # path('', book_list, name='book_list'),
    path('', BookListView.as_view(), name='book_list'),
    path('<slug:book>/', book_detail, name='book_detail'),
    path('<slug:book>/share/', book_share, name='book_share'),
    path('<slug:book>/review/', book_review, name='book_review'),
]
