from django.shortcuts import render, redirect
from foro.models import Pelicula, Videojuego, Cancion
from foro.forms import CrearVideojuego, CrearCancion

def inicio(request):
    
    return render(request, "foro/inicio.html", {})

def lobby(request):
    
    return render(request, "foro/lobby.html", {}) 

def peliculas(request):
    
    pelicula_a_buscar = request.GET.get('nombre')
    
    if pelicula_a_buscar:
        listado_de_peliculas = Pelicula.objects.filter(nombre__icontains=pelicula_a_buscar)
    else: 
        listado_de_peliculas = Pelicula.objects.all()
    
    return render(request, "foro/peliculas.html", {"listado_de_peliculas" : listado_de_peliculas}) 

def videojuegos(request):
    
    videojuego_a_buscar = request.GET.get('nombre')
    
    if videojuego_a_buscar:
        listado_de_videojuegos = Videojuego.objects.filter(nombre__icontains=videojuego_a_buscar)
    else:
        listado_de_videojuegos = Videojuego.objects.all()
    
    return render(request, "foro/videojuegos.html", {"listado_de_videojuegos" : listado_de_videojuegos}) 

def canciones(request):
    
    cancion_a_buscar = request.GET.get('nombre')
    
    if cancion_a_buscar:
        listado_de_canciones = Cancion.objects.filter(nombre__icontains=cancion_a_buscar)
    else:
        listado_de_canciones = Cancion.objects.all()
    
    return render(request, "foro/canciones.html", {"listado_de_canciones" : listado_de_canciones}) 

def menu_creacion(request):
    
    return render(request, "foro/menu_creacion.html", {})

def creacion_pelicula(request):
    
    if request.method == "POST":
        
        pelicula = Pelicula(nombre=request.POST.get('nombre'),
                            director=request.POST.get('director'),
                            titulo=request.POST.get('titulo'),
                            subtitulo=request.POST.get('subtitulo'),
                            opinion=request.POST.get('opinion'),
                            puntaje=request.POST.get('puntaje'))
        pelicula.save()
        
        return redirect('menu_creacion')
        
    return render(request, "foro/creacion_pelicula.html", {})

def creacion_videojuego(request):
    
    if request.method == "POST":
        
        formulario = CrearVideojuego(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            videojuego = Videojuego(nombre=info_limpia.get('nombre'),
                            desarrollador=info_limpia.get('desarrollador'),
                            titulo=info_limpia.get('titulo'),
                            subtitulo=request.get('subtitulo'),
                            opinion=info_limpia.get('opinion'),
                            puntaje=info_limpia.get('puntaje'))
            videojuego.save()
            
            return redirect('menu_creacion')
        else:
            return render(request, "foro/creacion_videojuego.html", {'formulario': formulario})
        
    formulario = CrearVideojuego()   
    return render(request, "foro/creacion_videojuego.html", {'formulario': formulario})

def creacion_cancion(request):
    
    if request.method == "POST":
        
        formulario = CrearCancion(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            cancion = Cancion(nombre=info_limpia.get('nombre'),
                            artista=info_limpia.get('artista'),
                            titulo=info_limpia.get('titulo'),
                            subtitulo=info_limpia.get('subtitulo'),
                            opinion=info_limpia.get('opinion'),
                            puntaje=info_limpia.get('puntaje'))
            cancion.save()
            
            return redirect('menu_creacion')
        else:
            return render(request, "foro/creacion_cancion.html", {'formulario': formulario})
    
    formulario = CrearCancion() 
    return render(request, "foro/creacion_cancion.html", {'formulario': formulario})