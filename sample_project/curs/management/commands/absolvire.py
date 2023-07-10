from django.core.management import BaseCommand
from django.db.models import F
from curs.models import Student

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        studenti = Student.objects.all()
        numar_studenti = studenti.update(an=F('an')+1)
        print(f"S-au modificat {numar_studenti} studenti")
