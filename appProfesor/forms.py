from django import forms
from appProfesor.models import Profesor

class FormProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'