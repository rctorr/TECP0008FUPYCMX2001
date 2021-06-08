"""Bedutravels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework import routers

from tours import views
from tours.schema import schema

# Agregando rutas para DjangoRest
router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("zonas", views.ZonaViewSet)
router.register("tours", views.TourViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', include("tours.urls")),
    path('wp-admin/', admin.site.urls),
]
