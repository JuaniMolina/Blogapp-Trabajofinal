from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from Blogapp.forms import PostForm

# Create your views here.

def inicio (request):
    return render(request, 'Blogapp/inicio.html')


#  Views relacionadas a los posteos 
def posteos (request):
    return render(request, 'Blogapp/posteos.html')    

def lista_posteos (request):
    posteos = Post.objects.all()
    if len(posteos) != 0:
        return render(request, 'Blogapp/lista_posteos.html', {'posteos': posteos})
    else:
        return render(request, 'Blogapp/lista_posteos.html', {'mensaje': 'Todavía no hay posteos'}) 

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
            
            return render(request, 'Blogapp/mostrarPost.html', {'post': post})
        else:
            return render(request, 'Blogapp/postFormulario.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'Blogapp/postFormulario.html', {'form': form})

def mostrarPost(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'Blogapp/mostrarPost.html', {'post': post})

def borrar_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return render(request, 'Blogapp/borrar_post.html', {'mensaje': 'Post borrado exitosamente'})

def editar_post (request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            post.titulo = info["titulo"]
            post.subtitulo = info['subtitulo']
            post.cuerpo = info['cuerpo']
            post.autor = info['autor']
            post.fecha = info['fecha']
            post.imagen = info['imagen']
            post.save()
            posteos = Post.objects.all()
            return render(request, 'Blogapp/lista_posteos.html', {'mensaje': 'Post editado exitosamente', 'posteos': posteos})        
    else:
        form = PostForm(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'cuerpo': post.cuerpo, 'autor': post.autor, 'fecha': post.fecha, 'imagen': post.imagen})
        return render(request, 'Blogapp/editar_post.html', {'form': form, 'post': post})

def about (request):
    return render(request, 'Blogapp/about.html')