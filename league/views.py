from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
            nextRoute = request.GET.get("next", "/")
            return redirect(nextRoute)
        else:
            message = form.errors
    else:
        form = AuthenticationForm()

    context = {"form": form, "message": message}
    return render(request, "league/login.html", context)


def index(request):
    return render(request, "league/index.html")


@login_required
def profile(request):
    team = Team.objects.get(owner=request.user)
    context = {"team": team}
    return render(request, "league/profile.html", context)


@login_required
def team_creation(request):
    userTeams = Team.objects.filter(owner=request.user)
    if len(userTeams) > 0:
        return redirect("/team")
    userTeamName = request.GET.get("team-name", "")
    if not userTeamName:
        return render(request, "league/teamcreation.html")
    else:
        try:
            team = Team(name=userTeamName, owner=request.user)
            team.save()
            return redirect("/")
        except:
            context = {"error_message": "Team name is already taken"}
            return render(request, "league/teamcreation.html", context)
