from django.contrib.sitemaps import Sitemap
from .models import Book
from django.urls import reverse
from taggit.models import Tag

class BookSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Book.published.all()
    
    def lastmod(self, obj):
        return obj.updated
    
class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6           

    def items(self):
        return Tag.objects.filter(
            book__in=Book.published.all()  
        ).distinct()

    def location(self, obj):
        return reverse('catalog:book_list_by_tag', args=[obj.slug])

    def lastmod(self, obj):
        latest = (
            Book.published.filter(tags__in=[obj])
            .order_by('-updated')
            .values_list('updated', flat=True)
            .first()
        )
        return latest