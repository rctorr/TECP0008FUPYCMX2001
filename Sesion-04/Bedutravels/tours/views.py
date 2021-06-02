from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tour, Zona

# Create your views here.
def index(request):
    """ Atender la petición GET / """
    # Consulta para obtener todos los elementos de un modelo / tabla
    # Regresa un QuerySet es una lista de objetos de tipo Tour
    lista_tours = Tour.objects.all()

    return render(request, "tours/index.html", {"tours": lista_tours})


@login_required
def zonas(request):
    """ Atender la petición GET /zonas/ """
    zonas = Zona.objects.all()
    contexto = {
        "zonas": zonas,
    }

    return render(request, "tours/zonas.html", contexto)


def tours_profile(request):
    """ Atiende la petición GET /accounts/profile/ """

    return redirect("/")


def tour(request, tour_id):
    """ Atiende la petición GET /tour/tour_id/ """
    tour = Tour.objects.get(id=tour_id)
    usuario = request.user
    es_editor = usuario.groups.filter(name="editores").exists()

    contexto = {
        "tour": tour,
        "es_editor": es_editor,
    }

    return render(request, "tours/tour.html", contexto)


def tour_eliminar(request, tour_id):
    """ Atiende la petición GET /tour/tour_id/eliminar/ """

    # Validando quien puede eliminar tours
    usuario = request.user
    es_editor = usuario.groups.filter(name="editores").exists()
    if es_editor:
        tour = Tour.objects.get(id=tour_id)
        tour.delete()

    return redirect("/")


