from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Blog Post URLs
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("posts/delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),

    # Comment URLs
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/update/<int:pk>/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/delete/<int:pk>/", CommentDeleteView.as_view(), name="comment-delete"),
]
