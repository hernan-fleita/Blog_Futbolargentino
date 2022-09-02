from django.db import models

# Create your models here.

class Boca(models.Model):
    nombre=models.CharField(max_length=50)
    goles=models.IntegerField()
class River(models.Model):
    nombre=models.CharField(max_length=50)
    goles=models.IntegerField()
    
class Sanlorenzo(models.Model):
    nombre=models.CharField(max_length=50)
    goles=models.IntegerField()