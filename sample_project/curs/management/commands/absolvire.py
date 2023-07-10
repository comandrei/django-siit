from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.db.models import F
from curs.models import Student

class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        super().add_arguments(parser)
        parser.add_argument("an", type=int)
        parser.add_argument("ceva")
        parser.add_argument("--minimum", type=int, default=0)
        # Echivalent in Python
        def absolvire(an, ceva, minimum=0):
            pass
        #absolvire(7)

    def handle(self, *args, **options):
        studenti = Student.objects.all()
        an_minim = options['minimum']
        studenti = studenti.filter(an__gte=an_minim)
        #print(kwargs)
        print(f"Anul cerut este {options['an']}")
        print(f"Minimum cerut este {options['minimum']}")
        numar_studenti = studenti.update(an=F('an')+1)
        print(f"S-au modificat {numar_studenti} studenti")


