from django.contrib import admin
from .models import Facultad, Carrera

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    # Esto mostrará el ID, el Nombre de la Carrera y a qué Facultad pertenece
    list_display = ('id', 'nombre', 'facultad')
    
    # Agrega un filtro lateral derecho para segmentar carreras por facultad rápidamente
    list_filter = ('facultad',)
    
    # Permite buscar carreras por su nombre
    search_fields = ('nombre',)