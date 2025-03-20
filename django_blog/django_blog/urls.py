# django_blog/django_blog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # Include the blog app's URLs at the root
]
