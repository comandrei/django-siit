from django.db import models

# Create your models here.

class Profesor(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nume} {self.prenume} <{self.email}>"

class CursManager(models.Manager):
    def an_terminal(self):
        return self.filter(an=5)
    
class Curs(models.Model):
    durata = models.IntegerField(default=80)
    pret = models.FloatField(db_index=True)
    descriere = models.TextField(null=True, blank=True)
    nume = models.CharField(max_length=30, unique=True)
    creat = models.DateTimeField(auto_now_add=True)
    actualizat = models.DateTimeField(auto_now=True)
    logo = models.FileField(null=True, blank=True)
    activ = models.BooleanField(default=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    coordonator = models.OneToOneField(Profesor, null=True, blank=True, on_delete=models.CASCADE, related_name="coordonator")
    an = models.IntegerField(default=1)

    objects = CursManager()

    def __str__(self):
        return f"{self.nume} {self.profesor}"
    
class Student(models.Model):
    class Meta:
        ordering = ["prenume", "nume"]
        unique_together = ("prenume", "nume")

    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=10)
    cursuri = models.ManyToManyField(Curs)

    def __str__(self):
        return f"{self.prenume} {self.nume}"
