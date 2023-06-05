from django.db import models

# Create your models here.
class Curs(models.Model):
    durata = models.IntegerField(default=80)
    pret = models.FloatField()
    descriere = models.TextField()
    nume = models.CharField(max_length=30)