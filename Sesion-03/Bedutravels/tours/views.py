from django.shortcuts import render, redirect
from .models import Tour, Zona

# Create your views here.
def index(request):
    """ Atender la petición GET / """
    # Consulta para obtener todos los elementos de un modelo / tabla
    # Regresa un QuerySet es una lista de objetos de tipo Tour
    lista_tours = Tour.objects.all()

    return render(request, "tours/index.html", {"tours": lista_tours})


def zonas(request):
    """ Atender la petición GET /zonas/ """
    zonas = Zona.objects.all()
    contexto = {
        "zonas": zonas,
    }

    return render(request, "tours/zonas.html", contexto)


def login(request):
    """
        Atender la petición GET /login/
        Atender la petición POST /login/
    """
    # Procesando peticón GET
    # Definimos el mensaje de error por omisión
    msg = ""
    # Datos virtuales de usuario
    usuario_valido = ("dos", "dos")

    if request.method == "POST":
        # Se inicia el procesado de la petición POST
        usuario = request.POST.get("username")
        clave = request.POST.get("password")
        # print(">>>", usuario, clave)
        if usuario_valido == (usuario, clave):
            # El usuario es válido
            return redirect("/")
        else:
            # El usuario no es válido
            msg = "El usuario no es válido, inteta de nuevo"

    # Respuesta de la petición GET, POST
    return render(request, "tours/login.html", {"msg": msg})

