from django.db import models

# Create your models here.


class Score(models.model):
    player_name = models.CharField(max_length=15)
    player_score = models.IntegerField()

    

