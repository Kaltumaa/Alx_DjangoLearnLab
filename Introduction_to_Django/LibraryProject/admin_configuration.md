# Django Admin Configuration for the Book Model

## Steps to Register and Customize the Book Model in the Django Admin:

1. **Register the Book Model:**
   In `bookshelf/admin.py`, the Book model is imported and registered with a custom admin class.

2. **Custom Admin Configuration:**
   The custom admin class `BookAdmin` is defined to:
   - **list_display:** Show `title`, `author`, and `publication_year` in the admin list view.
   - **list_filter:** Enable filtering by `author` and `publication_year`.
   - **search_fields:** Allow searching by `title` and `author`.

   The code in `bookshelf/admin.py` is as follows:

   ```python
   from django.contrib import admin
   from .models import Book

   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'publication_year')
       list_filter = ('author', 'publication_year')
       search_fields = ('title', 'author')

   admin.site.register(Book, BookAdmin)
