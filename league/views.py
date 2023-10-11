from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.contrib.auth import authenticate, login

from league.models import Team


# Create your views here.
def signup(request):
    message = ""
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print("form is valid")
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            message = form.errors
    else:
        form = UserCreationForm()

    context = {"form": form, "message": message}
    return render(request, "league/signup.html", context)


def log_in(request):
    message = ""
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            print("form is valid")
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            message = form.errors
    else:
        form = AuthenticationForm()

    context = {"form": form, "message": message}
    return render(request, "league/login.html", context)


def index(request):
    return render(request, "league/index.html")


def profile(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        team = Team.objects.get(owner=request.user)
        context = {"team": team}
        return render(request, "league/profile.html", context)
