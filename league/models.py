from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LolTeam(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="lolteam")

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    TOP = "TP"
    JUNGLE = "JG"
    MID = "MD"
    ADC = "AD"
    SUPPORT = "SP"
    POSITION_CHOICES = [
        (TOP, "Top"),
        (JUNGLE, "Jungle"),
        (MID, "Mid"),
        (ADC, "ADC"),
        (SUPPORT, "Support"),
    ]
    name = models.CharField(max_length=30)
    lol_team = models.ForeignKey(LolTeam, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to="player")
    postion = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)

    def __str__(self) -> str:
        return self.name
