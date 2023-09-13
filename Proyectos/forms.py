from django import forms
 
class ProyectoFormulario(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()


class TareaFormulario(forms.Form):
    nombreTarea = forms.CharField()
    fechaInicio = forms.DateField()
    fechaTermino=forms.DateField()
    estado=forms.CharField()

class PmFormulario(forms.Form):
    nombre:forms.CharField()
    apellido:forms.CharField()
    email:forms.CharField()