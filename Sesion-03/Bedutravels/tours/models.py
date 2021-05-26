from django.conf import settings
from django.db import models


# Create your models here.
class Zona(models.Model):
    """ Definiendo la tabla Zona """
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)

    def __str__(self):
        """ Representación en cadena de texto de la clase Zona """
        return self.nombre


class Perfil(models.Model):
    """ Definiendo la tabla Perfil """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    fechaNacimiento = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        """ Representación en cadena de texto de la clase Perfil """
        return self.user.username


class Tour(models.Model):
    """ Define la tabla Tour """
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name="tours_llegada")

    def __str__(self):
        return self.nombre
