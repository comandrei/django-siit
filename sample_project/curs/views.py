from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Curs, Student, Profesor
from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from .forms import ContactForm, ProfesorForm, StudentForm

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
    toate_cursurile = toate_cursurile.only("nume", "profesor")
    return render(request, "cursuri.html", {"cursuri": toate_cursurile})

def curs(request, curs_id):
    try:
        cursul_meu = Curs.objects.get(id=curs_id)
        studenti = ["Gigel"]
        studenti = cursul_meu.student_set.all()
        return render(request, "curs.html", 
                      {"cursul_meu": cursul_meu, "studenti": studenti,
                       "dictionar": {"unu":1, "doi":2}})
    except Curs.DoesNotExist:
        return HttpResponse("Nu exista", status=404)
    
def studenti(request):
    studenti = Student.objects.all().prefetch_related("cursuri")
    # for student in studenti:
    #     student.an = student.an + 1
    #     student.save()
    #studenti.update(an=F('an')+1)
    return render(request, "studenti.html", {"studenti": studenti})

def main(request):
    return render(request, "base.html", {})

def profil(request):
    return render(request, "profil.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mesaj = "Formular validat"
        else:
            mesaj = "Formular invalid"
    else:
        form = ContactForm()
        mesaj = ""
    context = {
        "form": form,
        "mesaj": mesaj
    }
    return render(request, "contact.html", context)

def add_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfesorForm()
    context = {
        "form": form
    }
    return render(request, "add_profesor.html", context)

def edit_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    if request.method == "POST":
        form = ProfesorForm(data=request.POST, instance=profesor)
        if form.is_valid():
            form.save()
    else:
        form = ProfesorForm(instance=profesor)
    context = {
        "form": form
    }
    return render(request, "edit_profesor.html", context)


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect("/students/")
    else:
        form = StudentForm()
    context = {
        "form": form
    }
    return render(request, "add_student.html", context)