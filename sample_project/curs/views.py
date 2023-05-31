from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Curs

def salut(request):
    unu = 1 
    return HttpResponse("Salut!")

def salut_nume(request, nume):
    return HttpResponse(f"Salut {nume}!")

def cursuri(request):
    toate_cursurile = Curs.objects.all() # select * from cursuri;
    nume_cursuri = [f"<a href='/curs/{curs.id}'>{curs.nume}</a>" for curs in toate_cursurile]
    return HttpResponse(f"{nume_cursuri}")

def curs(request, curs_id):
    try:
        cursul_meu = Curs.objects.get(id=curs_id)
        return HttpResponse(f"{cursul_meu.nume} <br /> {cursul_meu.pret} <br /> {cursul_meu.descriere}")
    except Curs.DoesNotExist:
        return HttpResponse("Nu exista", status=404)