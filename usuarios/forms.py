from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True)    
    email=forms.CharField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)