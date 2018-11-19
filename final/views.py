from django.shortcuts import render
from django.contrib import messages
from final.models import Curso,Asignacion,Programa
from .forms import ProgramaForm

# Create your views here.
def ingresar_pensum(request):

    if request.method == "POST":

        formulario = ProgramaForm(request.POST)

        if formulario.is_valid():

            programa = Programa.objects.create(estudiante=formulario.cleaned_data['estudiante'], nombre_programa= formulario.cleaned_data['nombre_programa'],
            grado=formulario.cleaned_data['grado'], anio=formulario.cleaned_data['anio'])

            for curso_id in request.POST.getlist('cursos'):

                asignacion = Asignacion(curso_id=curso_id, programa_id = programa.id)

                asignacion.save()

            messages.add_message(request, messages.SUCCESS, 'Programa Guardada Exitosamente')

    else:

        formulario = ProgramaForm()

    return render(request, 'final/pensum_ingresar.html', {'formulario': formulario})