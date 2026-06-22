from django.contrib import admin
from django.contrib import messages  # <-- 1. ASEGÚRATE DE IMPORTAR MESSAGES AQUÍ
from .models import Facultad, Carrera, Materia

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        if "El facultad" in str(message):
            message = str(message).replace("El facultad", "La facultad").replace("fue agregado", "fue agregada")
        super().message_user(request, message, level, extra_tags, fail_silently)


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'facultad')
    list_filter = ('facultad',)
    search_fields = ('nombre',)

    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        if "El carrera" in str(message):
            message = str(message).replace("El carrera", "La carrera").replace("fue agregado", "fue agregada")
        super().message_user(request, message, level, extra_tags, fail_silently)


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        if "El materia" in str(message):
            message = str(message).replace("El materia", "La materia").replace("fue agregado", "fue agregada")
        super().message_user(request, message, level, extra_tags, fail_silently)
    