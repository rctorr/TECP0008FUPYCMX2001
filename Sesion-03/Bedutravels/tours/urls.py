from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('zonas/', views.zonas, name="zonas"),
    path('accounts/login/', views.tours_login, name="login"),
    path('accounts/logout/', views.tours_logout, name="logout"),
]
