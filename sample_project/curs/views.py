import json 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.
from .models import Curs, Student, Profesor
from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from .forms import ContactForm, LoginForm, ProfesorForm, StudentForm

def salut(request):
    unu = 1 
    return HttpResponse("Salut!")

def salut_nume(request, nume):
    return HttpResponse(f"Salut {nume}!")

@cache_page(30)
@login_required
def cursuri(request):
    an = request.GET.get("an")
    toate_cursurile = Curs.objects.all().order_by("-an")
    toate_cursurile = toate_cursurile.select_related("profesor")
    if an is not None:
        toate_cursurile = toate_cursurile.filter(Q(an__lte=int(an)) | Q(nume__contains="Curs"))
    toate_cursurile = toate_cursurile.only("nume", "profesor")
    return render(request, "cursuri.html", {"cursuri": toate_cursurile})

@login_required
def curs(request, curs_id):
    if "cos" not in request.session:
        request.session["cos"] = []
    try:
        cursul_meu = Curs.objects.get(id=curs_id)
        # request.session["cos"].append(cursul_meu.nume)
        cursuri = request.session["cos"]
        cursuri.append(cursul_meu.nume)
        request.session["cos"] = cursuri
        studenti = ["Gigel"]
        studenti = cursul_meu.student_set.all()
        return render(request, "curs.html", 
                      {"cursul_meu": cursul_meu, "studenti": studenti,
                       "dictionar": {"unu":1, "doi":2}})
    except Curs.DoesNotExist:
        return HttpResponse("Nu exista", status=404)
    
@login_required
def studenti(request):
    request.session["students_view"] = request.session.get("students_view", 0) + 1
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

@login_required
def add_student(request):
    profesor = request.GET.get("profesor")
    if request.method == "POST":
        form = StudentForm(request.POST, filter_prof=profesor)
        if form.is_valid():
            student = form.save()
            return redirect("/students/")
    else:
        form = StudentForm(filter_prof=profesor)
    context = {
        "form": form
    }
    return render(request, "add_student.html", context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")

def generare_nume():
    import time; time.sleep(3)
    return "Georgel"

def api_view(request):
    raspuns = cache.get("api_view")
    if raspuns:
        raspuns["cache"] = "HIT"
    else:
        raspuns = {
            "nume": generare_nume()
        }
        raspuns["cache"] = "MISS"
        cache.set("api_view", raspuns, 30)

    # User speficic customizations
    raspuns["username"] = request.user.username

    return HttpResponse(json.dumps(raspuns),
                        content_type="application/json")

def client_app(request):
    return render(request, "client_app.html", {})