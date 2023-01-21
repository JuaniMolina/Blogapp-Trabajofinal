from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Avatar
from .froms import Formulario_avatar

from Blogregistro.froms import FormularioRegistro, Formulario_Edicion_Usuario
from django.contrib.auth.decorators import login_required


# Create your views here.
def obtener_avatar(request):
    lista = Avatar.objects.filter(usuario=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = '/media/avatar/defecto.png'
    return avatar

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
                return render(request, 'Blogapp/inicio.html', {'mensaje': f'Bienvenido {username}', 'avatar': obtener_avatar(request)})
            else:
                return render(request, 'Blogapp/Login_usuario.html', {'form': form, 'mensaje': 'USUARIO o CONTRASEÑA incorrectos'})
        else:
            return render(request, 'Blogapp/Login_usuario.html', {'form': form, 'mensaje': 'USUARIO o CONTRASEÑA incorrectos'})
    else:
        form= AuthenticationForm()
        return render(request, 'Blogapp/Login_usuario.html', {'form': form})

@login_required
def editar_usuario(request):
    usuario=request.user
    if request.method == 'POST':
        form = Formulario_Edicion_Usuario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            return render(request, 'Blogapp/inicio.html', {'mensaje': f'{usuario.username} editado exitosamente', 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/editar_usuario.html', {'form': form, 'usuario': usuario.username, 'avatar': obtener_avatar(request)})
    else:
        form = Formulario_Edicion_Usuario(instance=usuario)
        return render(request, 'Blogapp/editar_usuario.html', {'form': form, 'usuario': usuario.username, 'avatar': obtener_avatar(request)})


def perfil_usuario (request):
    usuario = request.user
    form = Formulario_Edicion_Usuario(instance=usuario)
    return render(request, 'Blogapp/perfil_usuario.html', {'avatar': obtener_avatar(request)})

def agregar_avatar (request):
    if request.method == 'POST':
        form = Formulario_avatar(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(usuario=request.user, imagen=request.FILES['imagen'])
            avatarViejo= Avatar.objects.filter(usuario=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render (request, 'Blogapp/perfil_usuario.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Avatar agregado exitosamente'})
        else:
            return render (request, 'Blogapp/agregar_avatar.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Error al agregar el avatar'})
    else:
        form = Formulario_avatar()
        return render(request, 'Blogapp/agregar_avatar.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Agrega o modifica tu avatar'})



