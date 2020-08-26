from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenidos a los datos de los pollos de milpa criolla")




