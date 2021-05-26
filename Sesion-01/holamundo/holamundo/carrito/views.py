from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_carrito(request):
    """ Atiende la petición de la url /carrito/ """
    html_carrito = """
    <h1>Página del carrito de mensajes</h1>
    <hr />
    <ul>
      <li>Algún saludos</li>
      <li>Segundo saludo</li>
      <li>Último saludo</li>
    </ul>
    <hr />
    <a href="/">Ir a home</a>
    """
    return HttpResponse(html_carrito)
