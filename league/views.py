from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print("form is valid")
            form.save()
            message = "User Created!"
        else:
            message = form.errors
    else:
        form = UserCreationForm()

    context = {"form": form, "message": message}
    return render(request, "league/signup.html", context)
