from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from Blogapp.forms import PostForm

# Create your views here.

def inicio (request):
    return render(request, 'Blogapp/inicio.html')

def posteos (request):
    return render(request, 'Blogapp/posteos.html')    

def lista_posteos (request):
    posteos = Post.objects.all()
    return render(request, 'Blogapp/lista_posteos.html', {'posteos': posteos})


def postFormulario(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info['titulo']
            subtitulo = info['subtitulo']
            cuerpo = info['cuerpo']
            autor = info['autor']
            fecha = info['fecha']
            imagen = info['imagen']
            post = Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            post.save()
            posteos = Post.objects.all()
            return render(request, 'Blogapp/posteos.html', {'posteos': posteos, 'mensaje': 'Post creado exitosamente'})
        else:
            return render(request, 'Blogapp/postFormulario.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'Blogapp/postFormulario.html', {'form': form})