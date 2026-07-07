
from django.db import models

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    # ... tu código actual de Facultad ...
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    # ... tu código actual de Carrera ...
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    # ... tu código actual de Materia ...
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

# 👇 AGREGA ESTE NUEVO MODELO AL FINAL
class Malla(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='mallas', verbose_name="Carrera")
    anio = models.IntegerField(verbose_name="Año del Plan")
    # Relación Muchos a Muchos: Una malla tiene muchas materias, y una materia puede estar en varias mallas
    materias = models.ManyToManyField(Materia, related_name='mallas', verbose_name="Materias de la Malla")

    class Meta:
        verbose_name = "Malla Curricular"
        verbose_name_plural = "Mallas Curriculares"

    def __str__(self):
        return f"Malla {self.carrera.nombre} - Plan {self.anio}"