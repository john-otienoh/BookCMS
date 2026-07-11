from django.shortcuts import get_object_or_404, render
from .models import Book, ReaderFavourite, Review
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailBookForm, ReviewForm, SearchForm
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity,
)
# Create your views here.
def book_list(request, tag_slug=None):
    published_books = Book.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        published_books = published_books.filter(tags__in=[tag])

    paginator = Paginator(published_books, per_page=6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.paginator.num_pages > 1
    return render(request, 'catalog/book/list.html', {
        'page_obj': page_obj,
        'is_paginated': is_paginated,
        'books': page_obj,
        'tag': tag
    })


class BookListView(ListView):
    """
    Displays a paginated list of published books, optionally filtered by tag.
    """
    model = Book
    context_object_name = 'books'
    template_name = 'catalog/book/list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Book.published.all()
        self.tag = None
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            self.tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[self.tag])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

    def paginate_queryset(self, queryset, page_size):
        """custom paginate query_set to avoid 404 on out-of-range page numbers."""
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty()
        )
        page_number = self.request.GET.get(self.page_kwarg, 1)
        page_obj = paginator.get_page(page_number)
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())

def book_detail(request, book):
    book = get_object_or_404(
        Book,
        status=Book.Status.PUBLISHED,
        slug=book
    )
    reviews = book.reviews.filter(active=True)
    form = ReviewForm()
    book_tags_ids = book.tags.values_list('id', flat=True)
    similar_books = Book.published.filter(
        tags__in=book_tags_ids
    ).exclude(id=book.id)
    similar_books = similar_books.annotate(
        same_tags=Count('tags')
    ).order_by('-same_tags', '-publish')[:4]
    return render(
        request,
        "catalog/book/detail.html",
        {"book": book, 'reviews': reviews, 'form': form, 'similar_books': similar_books}
    )

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

def book_search(request):
    form = SearchForm()
    query = None
    results = []
    full_text_empty = False  
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = (
                SearchVector('title', weight='A') +
                SearchVector('synopsis', weight='B')
            )
            search_query = SearchQuery(query)
            results = (
                Book.published.annotate(
                    rank=SearchRank(search_vector, search_query)
                )
                .filter(rank__gte=0.3)          
                .order_by('-rank')
            )
            if not results:
                results = (
                    Book.published.annotate(
                        similarity=TrigramSimilarity('title', query)
                    )
                    .filter(similarity__gt=0.1)
                    .order_by('-similarity')
                )
                full_text_empty = True 

    return render(request, 'catalog/book/search.html', {
        'form': form,
        'query': query,
        'results': results,
        'full_text_empty': full_text_empty,
    })