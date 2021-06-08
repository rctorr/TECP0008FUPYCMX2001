from django.contrib import admin
from .models import Zona, Perfil, Tour


# Register your models here.
class ZonaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("nombre", "descripcion", "longitud", "latitud")


class PerfilAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("user", "fechaNacimiento", "tipo")


class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("nombre", "operador", "tipoDeTour", "pais",
                    "zonaSalida", "zonaLlegada")


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Tour, TourAdmin)
