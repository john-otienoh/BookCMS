import markdown
from django.contrib.syndication.views import Feed
import markdown 
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html 
from django.urls import reverse_lazy 
from .models import Book

class LatestBookFeed(Feed):
    title = 'BookShelf CMS'
    link = reverse_lazy('catalog:book_list')
    description = 'Newly added books.'
    def items(self):
        return Book.published.all()[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords_html(
            markdown.markdown(item.synopsis), 30
        )
    def item_pubdate(self, item):
        return item.publish
    
