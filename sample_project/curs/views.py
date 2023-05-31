from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def salut(request):
    unu = 1 
    return HttpResponse("Salut!")

def salut_nume(request, nume):
    return HttpResponse(f"Salut {nume}!")