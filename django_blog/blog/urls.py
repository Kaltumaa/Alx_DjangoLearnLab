from django.urls import path
from .views import PostListView, TaggedPostListView, SearchResultsView
from .views import search_view

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("tags/<str:tag_name>/", TaggedPostListView.as_view(), name="tagged-posts"),
    path("search/", SearchResultsView.as_view(), name="search-results"),
    path("search/", search_view, name="search"),
]
