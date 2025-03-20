"""
URL Configuration for the Book API.

This module maps the following endpoints to the corresponding views:
- GET /books/            => List all books
- GET /books/<int:pk>/   => Retrieve a single book by its ID
- POST /books/create/    => Create a new book (authenticated users only)
- PUT /books/<int:pk>/update/  => Update an existing book (authenticated users only)
- DELETE /books/<int:pk>/delete/ => Delete a book (authenticated users only)
"""

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
