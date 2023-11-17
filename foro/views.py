from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from foro.forms import CrearCancion, ModificarCancion, CrearPelicula, ModificarPelicula
from foro.models import Pelicula, Videojuego, Cancion

def lobby(request):
    
    return render(request, "foro/lobby.html", {}) 
@login_required
def peliculas(request):
    
    pelicula_a_buscar = request.GET.get('nombre')
    
    if pelicula_a_buscar:
        listado_de_peliculas = Pelicula.objects.filter(nombre__icontains=pelicula_a_buscar)
    else: 
        listado_de_peliculas = Pelicula.objects.all()
    
    return render(request, "foro/peliculas.html", {"listado_de_peliculas" : listado_de_peliculas}) 
@login_required
def videojuegos(request):
    
    videojuego_a_buscar = request.GET.get('nombre')
    
    if videojuego_a_buscar:
        listado_de_videojuegos = Videojuego.objects.filter(nombre__icontains=videojuego_a_buscar)
    else:
        listado_de_videojuegos = Videojuego.objects.all()
    
    return render(request, "foro/videojuegos.html", {"listado_de_videojuegos" : listado_de_videojuegos}) 
@login_required
def canciones(request):
    
    cancion_a_buscar = request.GET.get('nombre')
    
    if cancion_a_buscar:
        listado_de_canciones = Cancion.objects.filter(nombre__icontains=cancion_a_buscar)
    else:
        listado_de_canciones = Cancion.objects.all()
    
    return render(request, "foro/canciones.html", {"listado_de_canciones" : listado_de_canciones}) 
@login_required
def menu_creacion(request):
    
    return render(request, "foro/menu_creacion.html", {})
@login_required
def creacion_pelicula(request):
    
    if request.method == "POST":
        
        formulario = CrearPelicula(request.POST, request.FILES)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            pelicula = Pelicula(nombre=info_limpia.get('nombre'),
                            director=info_limpia.get('director'),
                            titulo=info_limpia.get('titulo'),
                            subtitulo=info_limpia.get('subtitulo'),
                            opinion=info_limpia.get('opinion'),
                            puntaje=info_limpia.get('puntaje'),
                            fecha=info_limpia.get('fecha'),
                            imagen =info_limpia.get('imagen'))
            pelicula.save()
            
            return redirect('menu_creacion')
        else:
            return render(request, "foro/creacion_pelicula.html", {'formulario': formulario})
        
    formulario = CrearPelicula()   
    return render(request, "foro/creacion_pelicula.html", {'formulario': formulario})

class creacion_videojuego(LoginRequiredMixin, CreateView):
    model = Videojuego
    template_name = "foro/creacion_videojuego.html"
    fields = ['nombre', 'desarrollador', 'titulo', 'subtitulo', 'opinion', 'puntaje', 'fecha', 'imagen']
    success_url = reverse_lazy('menu_creacion')    
@login_required
def creacion_cancion(request):
    
    if request.method == "POST":
        
        formulario = CrearCancion(request.POST, request.FILES)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            cancion = Cancion(nombre=info_limpia.get('nombre'),
                            artista=info_limpia.get('artista'),
                            titulo=info_limpia.get('titulo'),
                            subtitulo=info_limpia.get('subtitulo'),
                            opinion=info_limpia.get('opinion'),
                            puntaje=info_limpia.get('puntaje'),
                            fecha=info_limpia.get('fecha'),
                            imagen =info_limpia.get('imagen'))
            cancion.save()
            
            return redirect('menu_creacion')
        else:
            return render(request, "foro/creacion_cancion.html", {'formulario': formulario})
    
    formulario = CrearCancion() 
    return render(request, "foro/creacion_cancion.html", {'formulario': formulario})
@login_required
def eliminar_blog_pelicula(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    pelicula.delete()
    return redirect(peliculas)
@login_required
def eliminar_blog_videojuego(request, videojuego_id):
    videojuego = Videojuego.objects.get(id=videojuego_id)
    videojuego.delete()
    return redirect(videojuegos)
@login_required
def eliminar_blog_cancion(request, cancion_id):
    cancion = Cancion.objects.get(id=cancion_id)
    cancion.delete()
    return redirect(canciones)    
@login_required
def modificar_blog_pelicula(request, pelicula_id):
    pelicula_a_actualizar = Pelicula.objects.get(id = pelicula_id)
    
    if request.method == "POST":
        formulario = ModificarPelicula(request.POST, request.FILES)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            pelicula_a_actualizar.nombre=info_nueva.get('nombre')
            pelicula_a_actualizar.director=info_nueva.get('director')
            pelicula_a_actualizar.titulo=info_nueva.get('titulo')
            pelicula_a_actualizar.subtitulo=info_nueva.get('subtitulo')
            pelicula_a_actualizar.opinion=info_nueva.get('opinion')
            pelicula_a_actualizar.puntaje=info_nueva.get('puntaje')
            pelicula_a_actualizar.fecha=info_nueva.get('fecha')
            pelicula_a_actualizar.imagen=info_nueva.get('imagen')
            
            pelicula_a_actualizar.save()
            
            return redirect('peliculas')
        return render(request, "foro/modificar_pelicula.html", {"formulario": formulario})
    
    formulario = ModificarPelicula(initial={'nombre': pelicula_a_actualizar.nombre,'director': pelicula_a_actualizar.artista,'titulo': pelicula_a_actualizar.titulo,'subtitulo': pelicula_a_actualizar.subtitulo,'opinion': pelicula_a_actualizar.opinion,'puntaje': pelicula_a_actualizar.puntaje,'fecha': pelicula_a_actualizar.fecha,'imagen': pelicula_a_actualizar.imagen})
    return render(request, "foro/modificar_pelicula.html", {"formulario": formulario})

class modificar_blog_videojuego(LoginRequiredMixin, UpdateView):
    model = Videojuego
    template_name = "foro/creacion_videojuego.html"
    fields = ['nombre', 'desarrollador', 'titulo', 'subtitulo', 'opinion', 'puntaje', 'fecha', 'imagen']
    success_url = reverse_lazy('menu_creacion')   
@login_required    
def modificar_blog_cancion(request, cancion_id):
    cancion_a_actualizar = Cancion.objects.get(id = cancion_id)
    
    if request.method == "POST":
        formulario = ModificarCancion(request.POST, request.FILES)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            cancion_a_actualizar.nombre=info_nueva.get('nombre')
            cancion_a_actualizar.artista=info_nueva.get('artista')
            cancion_a_actualizar.titulo=info_nueva.get('titulo')
            cancion_a_actualizar.subtitulo=info_nueva.get('subtitulo')
            cancion_a_actualizar.opinion=info_nueva.get('opinion')
            cancion_a_actualizar.puntaje=info_nueva.get('puntaje')
            cancion_a_actualizar.fecha=info_nueva.get('fecha')
            cancion_a_actualizar.imagen=info_nueva.get('imagen')
            
            cancion_a_actualizar.save()
            
            return redirect('canciones')
        return render(request, "foro/modificar_cancion.html", {"formulario": formulario})
    
    formulario = ModificarCancion(initial={'nombre': cancion_a_actualizar.nombre,'artista': cancion_a_actualizar.artista,'titulo': cancion_a_actualizar.titulo,'subtitulo': cancion_a_actualizar.subtitulo,'opinion': cancion_a_actualizar.opinion,'puntaje': cancion_a_actualizar.puntaje,'fecha': cancion_a_actualizar.fecha,'imagen': cancion_a_actualizar.imagen})
    return render(request, "foro/modificar_cancion.html", {"formulario": formulario})
@login_required
def detalle_pelicula(request, pelicula_id):
    pelicula = Pelicula.objects.get(id = pelicula_id)
    
    return render(request, "foro/detalle_pelicula.html", {"pelicula": pelicula})
@login_required    
def detalle_videojuego(request, videojuego_id):
    videojuego = Videojuego.objects.get(id = videojuego_id)
    
    return render(request, "foro/detalle_videojuego.html", {"videojuego": videojuego})
@login_required    
def detalle_cancion(request, cancion_id):
    cancion = Cancion.objects.get(id = cancion_id)
    
    return render(request, "foro/detalle_cancion.html", {"cancion": cancion})

def about_me(request):
    
    return render(request,'foro/aboutme.html',{})