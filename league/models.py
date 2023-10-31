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
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)

    def __str__(self) -> str:
        return self.name


class Statistics(models.Model):
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    turrets = models.IntegerField()
    inhibitors = models.IntegerField()
    dragonKills = models.IntegerField()
    baronKills = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    teamOne = models.CharField(max_length=30)
    teamTwo = models.CharField(max_length=30)
    teamOneScore = models.IntegerField()
    teamTwoScore = models.IntegerField()
    teamOneStats = Statistics
    teamTwoStats = Statistics

    def __str__(self) -> str:
        return self.name


class Week(models.Model):
    gameOne = Game
    gameTwo = Game
    gameThree = Game
    gameFour = Game
    gameFive = Game
    gameSix = Game
    gameSeven = Game
    gameEight = Game
    gameNine = Game
    gameTen = Game

    def __str__(self) -> str:
        return self.name


class Season(models.Model):
    weekOne = Week
    weekTwo = Week
    weekThree = Week
    weekFour = Week
    weekFive = Week
    weekSix = Week
    weekSeven = Week
    weekEight = Week

    def __str__(self) -> str:
        return self.name
