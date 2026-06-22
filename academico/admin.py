from django.contrib import admin
from .models import Facultad, Carrera, Materia  # <-- Asegúrate de importar Materia aquí

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'facultad')
    list_filter = ('facultad',)
    search_fields = ('nombre',)
    
    
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre')
    search_fields = ('codigo', 'nombre')