from django import forms
 
class ProyectoFormulario(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()