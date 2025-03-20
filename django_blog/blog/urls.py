# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Built-in views for login and logout
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    
    # Custom views for registration and profile management
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
