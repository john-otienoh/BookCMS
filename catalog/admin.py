from django.contrib import admin
from .models import Book,  ReaderFavourite, Review

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'added_by', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'added_by']
    search_fields = ['title', 'synopsis']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['added_by']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

# @admin.register(ReaderFavourite)
# class ReaderFavouriteAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'reader', 'book', 'created']
#     search_fields = ['book']
#     ordering = ['created']
#     show_facets = admin.ShowFacets.ALWAYS

@admin.register(Review) 
class ReviewAdmin(admin.ModelAdmin): 
    list_display = ['name', 'email', 'book', 'created', 'active'] 
    list_filter = ['active', 'created', 'updated'] 
    search_fields = ['name', 'email', 'body']
    show_facets = admin.ShowFacets.ALWAYS
