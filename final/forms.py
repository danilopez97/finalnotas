from django import forms
from .models import Curso, Programa

class ProgramaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Programa
        fields = ('estudiante','nombre_programa' ,'grado','anio','cursos')

        def __init__ (self, *args, **kwargs):
            super(ProgramaForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

            self.fields["cursos"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

            self.fields["cursos"].help_text = "Ingrese las materias del pensum"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

            self.fields["cursos"].queryset = Curso.objects.all()