from django.contrib import admin

from .models import Team, LolTeam, Player

admin.site.register(Team)
admin.site.register(LolTeam)
admin.site.register(Player)
# Register your models here.
