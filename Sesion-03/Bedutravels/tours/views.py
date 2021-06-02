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


def tours_login(request):
    """
        Atender la petición GET /login/
        Atender la petición POST /login/
    """
    # Procesando peticón GET
    # Definimos el mensaje de error por omisión
    msg = ""

    if request.method == "POST":
        # Se inicia el procesado de la petición POST
        usuario = request.POST.get("username")
        clave = request.POST.get("password")
        user = authenticate(request, username=usuario, password=clave)  # valida en la BD
        if user is not None:
            # El usuario es válido
            login(request, user)  # crea una galleta/cookie/sesión de usuario

            return redirect(request.GET.get("next", "/"))
        else:
            # El usuario no es válido
            msg = "El usuario no es válido, inteta de nuevo"

    # Respuesta de la petición GET, POST
    return render(request, "tours/login.html", {"msg": msg})


def tours_logout(request):
    """ Atiende la petición GET /accounts/logout/ """

    # Borrando las cookies / sesión
    logout(request)

    return redirect("/")
