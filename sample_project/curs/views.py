from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Curs, Student
from django.db.models import Q, F

def salut(request):
    unu = 1 
    return HttpResponse("Salut!")

def salut_nume(request, nume):
    return HttpResponse(f"Salut {nume}!")

def cursuri(request):
    an = request.GET.get("an")
    toate_cursurile = Curs.objects.all().order_by("-an")
    toate_cursurile = toate_cursurile.select_related("profesor")
    if an is not None:
        toate_cursurile = toate_cursurile.filter(Q(an__lte=int(an)) | Q(nume__contains="Curs"))
    
    return render(request, "cursuri.html", {"cursuri": toate_cursurile})

def curs(request, curs_id):
    try:
        cursul_meu = Curs.objects.get(id=curs_id)
        studenti = ["Gigel"]
        studenti = cursul_meu.student_set.all()
        return render(request, "curs.html", 
                      {"cursul_meu": cursul_meu, "studenti": studenti})
    except Curs.DoesNotExist:
        return HttpResponse("Nu exista", status=404)
    
def studenti(request):
    studenti = Student.objects.all().prefetch_related("cursuri")
    # for student in studenti:
    #     student.an = student.an + 1
    #     student.save()
    #studenti.update(an=F('an')+1)
    return render(request, "studenti.html", {"studenti": studenti})