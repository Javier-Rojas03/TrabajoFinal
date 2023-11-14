from django.urls import path
from foro.views import inicio, lobby, peliculas, videojuegos, canciones, menu_creacion,creacion_pelicula, creacion_videojuego, creacion_cancion


urlpatterns = [
    path('', inicio, name='inicio'),
    path('lobby/',  lobby, name='lobby'),
    path('peliculas/',  peliculas, name='peliculas'),
    path('videojuegos/',  videojuegos, name='videojuegos'),
    path('canciones/',  canciones, name='canciones'),
    path('creacion/', menu_creacion, name='menu_creacion'),
    path('creacion/pelicula', creacion_pelicula, name='creacion_pelicula'),
    path('creacion/videojuego', creacion_videojuego, name='creacion_videojuego'),
    path('creacion/cancion', creacion_cancion, name='creacion_cancion')
]
