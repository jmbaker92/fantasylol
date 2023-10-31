from django.core.management.base import BaseCommand, CommandError
import json

from league.models import LolTeam, Player


class Command(BaseCommand):
    help = "Seeds the database with inital teams."

    def handle(self, *args, **options):
        # read json file, loop over lolteams, create the lolteam object using django api, pass the image url and store in media files
        #
        fileHandler = open("league/management/commands/data.json", "r")
        data = json.loads(fileHandler.read())
        fileHandler.close()
        teams = data["lolteams"]
        for team in teams:
            currTeam = LolTeam(name=team["name"])
            currTeam.save()
            for player in team["players"]:
                name = player["name"]
                role = player["role"]

                currPlayer = Player(name=name, position=role, lol_team=currTeam)
                currPlayer.save()
