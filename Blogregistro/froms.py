from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label='Email Usuario', max_length=50)
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields} 

class Formulario_Edicion_Usuario(UserCreationForm):
    email = forms.EmailField(label='Email Usuario', max_length=50)
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields} 