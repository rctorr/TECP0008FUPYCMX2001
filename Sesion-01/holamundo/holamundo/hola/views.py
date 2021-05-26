from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    """ Atiende la petición del documento raíz / """
    respuesta = HttpResponse("<h2>Hola mundo desde Django</h2>")

    return respuesta

def adios(request):
    """ Atiende la petición del url /adios/ """
    return HttpResponse("<hr><h3>Adios bye!</h3>")
