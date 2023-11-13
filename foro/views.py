from django.shortcuts import render


def inicio(request):
    
    return render(request, "foro/inicio.html", {})

def peliculas(request):
    
    return render(request, "foro/peliculas.html", {}) 