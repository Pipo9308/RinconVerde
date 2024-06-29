# forms.py
from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    terminos = forms.BooleanField(label='He leído los términos', required=True)

    class Meta:
        model = Usuario
        fields = ['nombres', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        terminos = cleaned_data.get('terminos')

        if not terminos:
            self.add_error('terminos', 'Debes aceptar los términos para registrarte.')
