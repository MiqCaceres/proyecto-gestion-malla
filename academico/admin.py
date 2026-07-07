from django.contrib import admin
from django.contrib import messages 
from django.utils.safestring import mark_safe
from .models import Facultad, Carrera, Materia, Malla  # <-- ¡Asegúrate de importar Malla aquí!

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        message_str = str(message)
        if "El facultad" in message_str:
            message_str = message_str.replace("El facultad", "La facultad").replace("fue agregado", "fue agregada")
            message = mark_safe(message_str)
        super().message_user(request, message, level, extra_tags, fail_silently)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'facultad')
    list_filter = ('facultad',)
    search_fields = ('nombre',)
    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        message_str = str(message)
        if "El carrera" in message_str:
            message_str = message_str.replace("El carrera", "La carrera").replace("fue agregado", "fue agregada")
            message = mark_safe(message_str)
        super().message_user(request, message, level, extra_tags, fail_silently)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        message_str = str(message)
        if "El materia" in message_str:
            message_str = message_str.replace("El materia", "La materia").replace("fue agregado", "fue agregada")
            message = mark_safe(message_str)
        super().message_user(request, message, level, extra_tags, fail_silently)

# 👇 REGISTRA LA NUEVA CLASE AQUÍ ABAJO
@admin.register(Malla)
class MallaAdmin(admin.ModelAdmin):
    list_display = ('id', 'carrera', 'anio')
    list_filter = ('carrera', 'anio')
    
    # Esto crea una interfaz hermosa con dos columnas para pasar materias de izquierda a derecha
    filter_horizontal = ('materias',)

    # Corrección de género para "La malla... fue agregada"
    def message_user(self, request, message, level=messages.SUCCESS, extra_tags="", fail_silently=False):
        message_str = str(message)
        if "El malla" in message_str:
            message_str = message_str.replace("El malla", "La malla").replace("fue agregado", "fue agregada")
            message = mark_safe(message_str)
        super().message_user(request, message, level, extra_tags, fail_silently)