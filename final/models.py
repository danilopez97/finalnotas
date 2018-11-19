from django.db import models
from django.contrib import admin

class Curso(models.Model):
    nombre  =   models.CharField(max_length=250)
    profesor = models.CharField(max_length=250)
    descripcion=models.CharField(max_length=250)
    def __str__(self):
        return self.nombre
class Programa(models.Model):
    estudiante    = models.CharField(max_length=250)
    nombre_programa   = models.CharField(max_length=250)
    grado   = models.CharField(max_length=250)
    anio      = models.IntegerField()
    cursos   = models.ManyToManyField(Curso, through='Asignacion')
    def __str__(self):
        return self.estudiante



class Asignacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    nota = models.IntegerField()

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class ProgramaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,) 
 