from django.urls import path
from foro.views import inicio, lobby, peliculas, videojuegos, canciones, menu_creacion,creacion_pelicula, creacion_videojuego, creacion_cancion, eliminar_blog_pelicula, eliminar_blog_videojuego, eliminar_blog_cancion, modificar_blog_cancion, modificar_blog_pelicula, modificar_blog_videojuego


urlpatterns = [
    path('', inicio, name='inicio'),
    path('lobby/',  lobby, name='lobby'),
    path('peliculas/',  peliculas, name='peliculas'),
    path('videojuegos/',  videojuegos, name='videojuegos'),
    path('canciones/',  canciones, name='canciones'),
    path('creacion/', menu_creacion, name='menu_creacion'),
    path('creacion/pelicula', creacion_pelicula, name='creacion_pelicula'),
    path('creacion/videojuego', creacion_videojuego, name='creacion_videojuego'),
    path('creacion/cancion', creacion_cancion, name='creacion_cancion'),
    path('peliculas/<int:pelicula_id>/eliminar', eliminar_blog_pelicula, name='eliminar_blog_pelicula'),
    path('videojuegos/<int:videojuego_id>/eliminar', eliminar_blog_videojuego, name='eliminar_blog_videojuego'),
    path('canciones/<int:cancion_id>/eliminar', eliminar_blog_cancion, name='eliminar_blog_cancion'),
    path('peliculas/<int:pelicula_id>/modificar', modificar_blog_pelicula, name='modificar_blog_pelicula'),
    path('videojuegos/<int:videojuego_id>/modificar', modificar_blog_videojuego, name='modificar_blog_videojuego'),
    path('canciones/<int:cancion_id>/modificar', modificar_blog_cancion, name='modificar_blog_cancion')
]
