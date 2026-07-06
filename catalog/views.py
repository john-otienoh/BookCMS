from django.shortcuts import get_object_or_404, render
from .models import Book, ReaderFavourite

# Create your views here.
def book_list(request):
    books = Book.published.all()
    return render(
        request,
        "catalog/book/list.html",
        {"books": books}
    )

def book_detail(request, id):
    book = get_object_or_404(Book, id=id, status=Book.Status.PUBLISHED)
    return render(
        request,
        "catalog/book/detail.html",
        {"book": book}
    )