from django.urls import path
from .views import (
    PostListView, PostDetailView, CommentCreateView, 
    CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/", BookCreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),

    # ✅ Updated to match the expected structure
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),  
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
