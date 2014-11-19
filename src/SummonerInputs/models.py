from django.db import models

# Create your models here.
class SummonerInput (models.Model):
    Summoner = models.CharField(max_length=30, blank = False, null = True)