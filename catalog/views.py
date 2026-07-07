from django.shortcuts import get_object_or_404, render
from .models import Book, ReaderFavourite, Review
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailBookForm, ReviewForm
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

# Create your views here.
def book_list(request):
    published_books = Book.published.all()
    paginator = Paginator(published_books, per_page=4)
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
    reviews = book.reviews.filter(active=True)
    form = ReviewForm()
    return render(
        request,
        "catalog/book/detail.html",
        {"book": book, 'reviews': reviews, 'form': form}
    )


class BookListView(ListView):
    """
    Displays a paginated list of published books.
    """
    model = Book                                
    context_object_name = 'books'                 
    template_name = 'catalog/book/list.html'      
    paginate_by = 4                             

    def get_queryset(self):
        return Book.published.all()
    
    def paginate_queryset(self, queryset, page_size):
        """custom paginate query_set to avoid 404 on out-of-range page numbers."""
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty()
        )
        page_number = self.request.GET.get(self.page_kwarg, 1)
        page_obj = paginator.get_page(page_number)
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())
    
def book_share(request, book):
    book = get_object_or_404(
        Book, slug=book, status=Book.Status.PUBLISHED
    )
    sent = False
    if request.method == 'POST':
        form = EmailBookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book_url = request.build_absolute_uri(
                book.get_absolute_url()
            )
            subject = (f"{cd['name']} ({cd['email']}) " f"recommends you read {book.title}")
            message = (
                f"Read {book.title} at {book_url}\n\n"
                f"{cd['name']}'s reviews: {cd['reviews']}"
            )
            send_mail(subject=subject, message=message, from_email=None, recipient_list=[cd['to']])
            sent = True
    else:   
        form = EmailBookForm()

    return render(
        request,
        'catalog/book/share.html',
        {'book': book, 'form': form, 'sent': sent}
    )

@require_POST
def book_review(request, book):
    book = get_object_or_404(
        Book, slug=book, status=Book.Status.PUBLISHED
    )
    review = None
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()

    return render(
    request, 'catalog/book/review.html', 
    {'book': book, 'review': review, 'form': form}
)