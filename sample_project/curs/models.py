from django.db import models

# Create your models here.
class Curs(models.Model):
    durata = models.IntegerField()
    pret = models.FloatField()
    descriere = models.TextField()
    nume = models.CharField(max_length=30)