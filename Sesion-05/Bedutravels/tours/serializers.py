from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Zona, Tour


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las converiones para el modelo User """
    class Meta:
        # Se define el modelo relacionado
        model = User
        # Lista de campos a inclur en la conversión
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'email')


class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las converiones para el modelo Tour """
    class Meta:
        # Se define el modelo relacionado
        model = Tour
        # Lista de campos a inclur en la conversión
        fields = ('id', 'nombre', 'slug', 'operador', 'tipoDeTour',
                  'descripcion', 'pais', 'zonaSalida', 'zonaLlegada')


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las converiones para el modelo Zona """

    # Define la relación de una Zona con sus Tours
    tours_salida = TourSerializer(many=True, read_only=True)
    tours_llegada = TourSerializer(many=True, read_only=True)

    class Meta:
        # Se define el modelo relacionado
        model = Zona
        # Lista de campos a inclur en la conversión
        fields = ('id', 'nombre', 'descripcion', 'longitud', 'latitud',
                  'tours_salida', 'tours_llegada')


