from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostByTagListView,  # ✅ Ensure this view exists in views.py
    SearchResultsView,
    search_view,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="tagged-posts"),  # ✅ Fixed slug format and view name
    path("search/", SearchResultsView.as_view(), name="search-results"),
    path("search/", search_view, name="search"),
]
