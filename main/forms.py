from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email"]