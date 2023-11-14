from django.shortcuts import render, redirect
from foro.models import Pelicula, Videojuego, Cancion
from foro.forms import CrearVideojuego, CrearCancion, ModificarCancion, ModificarVideojuego

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
                            subtitulo=info_limpia.get('subtitulo'),
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

def eliminar_blog_pelicula(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    pelicula.delete()
    return redirect(peliculas)

def eliminar_blog_videojuego(request, videojuego_id):
    videojuego = Videojuego.objects.get(id=videojuego_id)
    videojuego.delete()
    return redirect(videojuegos)

def eliminar_blog_cancion(request, cancion_id):
    cancion = Cancion.objects.get(id=cancion_id)
    cancion.delete()
    return redirect(canciones)    

def modificar_blog_pelicula(request, pelicula_id):
    pelicula_a_actualizar = Pelicula.objects.get(id = pelicula_id)
    
    if request.method == "POST":
        pelicula_a_actualizar.nombre=request.POST.get('nombre')
        pelicula_a_actualizar.director=request.POST.get('director')
        pelicula_a_actualizar.titulo=request.POST.get('titulo')
        pelicula_a_actualizar.subtitulo=request.POST.get('subtitulo')
        pelicula_a_actualizar.opinion=request.POST.get('opinion')
        pelicula_a_actualizar.puntaje=request.POST.get('puntaje')

        pelicula_a_actualizar.save()
        return redirect('peliculas')
    
    
    return render(request, "foro/modificar_pelicula.html", {"pelicula_a_actualizar": pelicula_a_actualizar})

def modificar_blog_videojuego(request, videojuego_id):
    videojuego_a_actualizar = Videojuego.objects.get(id = videojuego_id)
    
    if request.method == "POST":
        formulario = ModificarVideojuego(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            videojuego_a_actualizar.nombre=info_nueva.get('nombre')
            videojuego_a_actualizar.desarrollador=info_nueva.get('desarrollador')
            videojuego_a_actualizar.titulo=info_nueva.get('titulo')
            videojuego_a_actualizar.subtitulo=info_nueva.get('subtitulo')
            videojuego_a_actualizar.opinion=info_nueva.get('opinion')
            videojuego_a_actualizar.puntaje=info_nueva.get('puntaje')
            
            videojuego_a_actualizar.save()
            
            return redirect('videojuegos')
        return render(request, "foro/modificar_videojuego.html", {"formulario": formulario})
    
    formulario = ModificarVideojuego(initial={'nombre':videojuego_a_actualizar.nombre,'desarrollador':videojuego_a_actualizar.desarrollador,'titulo':videojuego_a_actualizar.titulo,'subtitulo':videojuego_a_actualizar.subtitulo,'opinion':videojuego_a_actualizar.opinion,'puntaje':videojuego_a_actualizar.puntaje})
    return render(request, "foro/modificar_videojuego.html", {"formulario": formulario})
    
def modificar_blog_cancion(request, cancion_id):
    cancion_a_actualizar = Cancion.objects.get(id = cancion_id)
    
    if request.method == "POST":
        formulario = ModificarCancion(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            cancion_a_actualizar.nombre=info_nueva.get('nombre')
            cancion_a_actualizar.artista=info_nueva.get('artista')
            cancion_a_actualizar.titulo=info_nueva.get('titulo')
            cancion_a_actualizar.subtitulo=info_nueva.get('subtitulo')
            cancion_a_actualizar.opinion=info_nueva.get('opinion')
            cancion_a_actualizar.puntaje=info_nueva.get('puntaje')
            
            cancion_a_actualizar.save()
            
            return redirect('canciones')
        return render(request, "foro/modificar_cancion.html", {"formulario": formulario})
    
    formulario = ModificarCancion(initial={'nombre': cancion_a_actualizar.nombre,'artista': cancion_a_actualizar.artista,'titulo': cancion_a_actualizar.titulo,'subtitulo': cancion_a_actualizar.subtitulo,'opinion': cancion_a_actualizar.opinion,'puntaje': cancion_a_actualizar.puntaje})
    return render(request, "foro/modificar_cancion.html", {"formulario": formulario})