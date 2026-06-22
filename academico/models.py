from django.db import models

class Facultad(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Facultades"

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='carreras')

    def __str__(self):
        return f"{self.nombre} ({self.facultad.nombre})"

class Materia(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"

class MallaCurricular(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='mallas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    año = models.PositiveIntegerField(help_text="Año de la carrera (ej. 1, 2, 3)")
    semestre = models.PositiveIntegerField(help_text="Semestre (ej. 1, 2)")

    def __str__(self):
        return f"{self.carrera.nombre} - {self.materia.nombre} ({self.año}° Año)"
    
    class Meta:
        verbose_name = "Malla Curricular"
        verbose_name_plural = "Mallas Curriculares"