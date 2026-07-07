from django.shortcuts import get_object_or_404, render
from .models import Book, ReaderFavourite
from django.core.paginator import Paginator

# Create your views here.
def book_list(request):
    published_books = Book.published.all()
    paginator = Paginator(published_books, per_page=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.paginator.num_pages > 1 
    return render(request, 'catalog/book/list.html', {
        'page_obj': page_obj,
        'is_paginated': is_paginated,
        'books': page_obj,
    }) 


def book_detail(request, book):
    book = get_object_or_404(
        Book,
        status=Book.Status.PUBLISHED,
        slug=book
    )
    return render(
        request,
        "catalog/book/detail.html",
        {"book": book}
    )
