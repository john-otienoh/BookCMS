from django.urls import path
from .views import book_list, book_detail, BookListView, book_share, book_review, book_search
from .feeds import LatestBookFeed

app_name = 'catalog'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('feed/', LatestBookFeed(), name='book_feed'),
    # path('', BookListView.as_view(), name='book_list'),
    path('tag/<slug:tag_slug>/', book_list, name='book_list_by_tag'),
    path('search/', book_search, name='book_search'),
    path('<slug:book>/', book_detail, name='book_detail'),
    path('<slug:book>/share/', book_share, name='book_share'),
    path('<slug:book>/review/', book_review, name='book_review'),   
]
