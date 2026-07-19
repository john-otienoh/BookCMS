from django import template
from ..models import Book
from taggit.models import Tag
import markdown
from django.utils.safestring import mark_safe
from django.db.models import Count
      

register = template.Library()

@register.simple_tag
def total_books():
    return Book.published.count()

@register.inclusion_tag('catalog/book/latest_books.html')
def show_latest_books(count=4):
    latest_books = Book.published.order_by('-publish')[:count]
    return {'latest_books': latest_books}

@register.simple_tag
def get_most_reviewed_books(count=4):
    return Book.published.annotate(
        total_reviews=Count('reviews')
    ).order_by('-total_reviews')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.inclusion_tag('catalog/book/tag_list.html')
def show_all_tags():
    tags = Tag.objects.all()
    return {'tags': tags}