"""
URL configuration for fantasylol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from fantasylol import settings
from league import views
from league.views import log_in
from django.conf.urls.static import static

urlpatterns = [
    path("api/draft-players/", views.draft_players, name="draftplayers"),
    path("team/user/", views.user_team, name="userteam"),
    path("accounts/profile/", views.profile, name="profilepage"),
    path("", views.index, name="homepage"),
    path("accounts/login/", views.log_in, name="login"),
    path("admin/", admin.site.urls),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("team/new/", views.team_creation, name="newteam"),
    path("team/draft/", views.draft, name="draft"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
