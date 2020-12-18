from django.db import models

#CharField, IntegerField, FloatField, DateField, ImageField 
# Create your models here.

#Player name
class PlayerName(models.Model):
    name = models.CharField(max_length = 255)


class PlayerStat(models.Model):
    avg = models.FloatField(max_length = 255)
    ops = models.FloatField(max_length = 255)