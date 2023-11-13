from django.urls import path
from foro.views import inicio, peliculas


urlpatterns = [
    path('', inicio),
    path('peliculas/',  peliculas)
]
