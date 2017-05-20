from django.db import models

# Create your models here.


class Score(models.Model):
    player_name = models.CharField(max_length=15)
    player_score = models.IntegerField()


    def __str__(self):
        return self.player_name


