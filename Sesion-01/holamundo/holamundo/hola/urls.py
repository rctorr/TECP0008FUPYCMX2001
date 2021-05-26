from django.urls import path
from . import views  # vistas de la app hola

urlpatterns = [
    path('', views.home, name="home"),  # / -> views.home()
    path('adios/', views.adios, name="adios"),  # /adios/ -> views.adios()
]
