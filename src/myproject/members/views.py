from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)          
            return redirect("/")
        else:
            messages.success(request, ("There was an error logging in, try again"))
            return redirect("login_user")
    else:
        return render(request,"auth/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You logged out"))
    return redirect("/")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesful"))
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "auth/register_user.html", {"form": form})