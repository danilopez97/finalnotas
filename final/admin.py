from django.contrib import admin
from final.models import Curso,CursoAdmin,Programa,ProgramaAdmin
# Register your models here.

admin.site.register(Curso, CursoAdmin)
admin.site.register(Programa, ProgramaAdmin)