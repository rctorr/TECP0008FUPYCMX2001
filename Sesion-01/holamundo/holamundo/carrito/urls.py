from django.urls import path
from . import views  # vistas de la app carrito 

urlpatterns = [
    path('', views.home_carrito, name="home_carrito"),  # / -> views.home_carrito()
]
