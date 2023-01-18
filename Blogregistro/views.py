from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from Blogregistro.froms import FormularioRegistro


# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form= FormularioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'Blogapp/inicio.html', {'form': form, 'mensaje': 'Usuario creado exitosamente'})
        else:
            return render(request, 'Blogapp/Registro_usuario.html', {'form': form, 'mensaje': 'Error al crear el usuario'})   
    else:
        form= FormularioRegistro()
        return render(request, 'Blogapp/Registro_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion_usuario = form.cleaned_data
            username = informacion_usuario['username']
            password = informacion_usuario['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'Blogapp/inicio.html', {'mensaje': f'Bienvenido {username}'})
            else:
                return render(request, 'Blogapp/Login_usuario.html', {'form': form, 'mensaje': 'USUARIO o CONTRASEÑA incorrectos'})
        else:
            return render(request, 'Blogapp/Login_usuario.html', {'form': form, 'mensaje': 'USUARIO o CONTRASEÑA incorrectos'})
    else:
        form= AuthenticationForm()
        return render(request, 'Blogapp/Login_usuario.html', {'form': form})

