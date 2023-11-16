from django.db import models
from ckeditor.fields import RichTextField

class Pelicula(models.Model):
   nombre = models.CharField(max_length=30)
   director = models.CharField(max_length=20)
   titulo = models.CharField(max_length=100)
   subtitulo = models.CharField(max_length=200)
   opinion = RichTextField()
   puntaje = models.DecimalField(max_digits=3,decimal_places=1)
   fecha = models.DateField()
   imagen = models.ImageField(upload_to='img_peliculas', null=True, blank=True)
   # contemplar idea de autor
   def __str__(self):
       return f'{self.id} - {self.nombre} - {self.puntaje}'

class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    opinion = RichTextField()
    puntaje = models.DecimalField(max_digits=3,decimal_places=1)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='img_videojuegos', null=True, blank=True)
    # contemplar idea de autor
    def __str__(self):
       return f'{self.id} - {self.nombre} - {self.puntaje}'
    
class Cancion(models.Model):
    nombre = models.CharField(max_length=30)
    artista = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    opinion = RichTextField()
    puntaje = models.DecimalField(max_digits=3,decimal_places=1)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='img_canciones', null=True, blank=True)
    # contemplar idea de autor
    def __str__(self):
       return f'{self.id} - {self.nombre} - {self.puntaje}'
