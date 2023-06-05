from django.db import models

# Create your models here.
class Curs(models.Model):
    durata = models.IntegerField(default=80)
    pret = models.FloatField(db_index=True)
    descriere = models.TextField(null=True, blank=True)
    nume = models.CharField(max_length=30, unique=True)
    creat = models.DateTimeField(auto_now_add=True)
    actualizat = models.DateTimeField(auto_now=True)
    logo = models.FileField(null=True, blank=True)
    activ = models.BooleanField(default=True)

class Profesor(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=10)