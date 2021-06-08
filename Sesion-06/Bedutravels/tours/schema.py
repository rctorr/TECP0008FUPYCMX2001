from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType

import graphene

from .models import Zona, Tour


class UserType(DjangoObjectType):
    """ Tipo de dato para manejar el modelo/tabla User """
    class Meta:
        model = User


class ZonaType(DjangoObjectType):
    """ Tipo de dato para manejar el modelo/tabla Zona """
    class Meta:
        model = Zona


class TourType(DjangoObjectType):
    """ Tipo de dato para manejar el modelo/tabla Tour """
    class Meta:
        model = Tour


class Query(graphene.ObjectType):
    """ Definir las consultas posibles y sus respuestas """

    # Se definen las posibles consultas
    all_users = graphene.List(UserType)
    all_zonas = graphene.List(ZonaType)
    all_tours = graphene.List(TourType)

    # Se definen las respuestas las consultas
    def resolve_all_users(self, info, **kwargs):
        """ Responder a la consulta all_users """
        return User.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        """ Responder a la consulta all_zonas """
        return Zona.objects.all()

    def resolve_all_tours(self, info, **kwargs):
        """ Responder a la consulta all_tours """
        return Tour.objects.all()


class CrearZona(graphene.Mutation):
    """ Permite crear un registro en la tabla/model Zona """
    class Arguments:
        """ Define los argumentos para crear una Zona """
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        longitud = graphene.Decimal()
        latitud = graphene.Decimal()

    # El atributo usado para la respuesta
    zona = graphene.Field(ZonaType)

    def mutate(self, info, nombre, descripcion=None, latitud=None, longitud=None):
        """ Se encarga de crear el registro de una Zona """
        zona = Zona(
            nombre=nombre,
            descripcion=descripcion,
            latitud=latitud,
            longitud=longitud
        )
        zona.save()

        return CrearZona(zona=zona)


class Mutations(graphene.ObjectType):
    """ Para agrupar todas las mutaciones """
    crear_zona = CrearZona.Field()


# Se crea el esquema que hace vincula todas las clases anteriores
schema = graphene.Schema(query=Query, mutation=Mutations)

