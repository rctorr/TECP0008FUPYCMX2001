from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('zonas/', views.zonas, name="zonas"),
    path('login/', views.login, name="login"),
]
