from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    # Add filters for better navigation
    list_filter = ('author', 'publication_year')
    # Enable search on title and author fields
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
