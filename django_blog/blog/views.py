# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    """
    Handle user registration. If the form is valid, create a new user and log them in.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    """
    Allow authenticated users to view and update their profile details.
    Currently, this view allows updating the user's email.
    """
    if request.method == "POST":
        new_email = request.POST.get("email")
        if new_email:
            request.user.email = new_email
            request.user.save()
    return render(request, "blog/profile.html")
