from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.Status.PUBLISHED)

# Create your models here.
class Book(models.Model):
    """Creating Book model"""
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    synopsis = models.TextField()
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='books_added'
    )
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)
    objects = models.Manager() 
    published = PublishedManager()

    # an editorial/CMS date, not the book's real print date
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def natural_key(self):
        return (self.slug,)
    
    def get_absolute_url(self):
        return reverse(
            'catalog:book_detail', 
            args=[
                self.slug,
            ] 
        )
    
    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=['-publish'])]

class ReaderFavourite(models.Model):
    pk = models.CompositePrimaryKey("reader", "book")
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reader} - {self.book}"


class Review(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]
    def __str__(self):
        return f'Review by {self.name} on {self.book}'