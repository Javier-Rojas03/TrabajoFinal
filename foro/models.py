from django.db import models


# idea es crear foro donde opinen sobro media consumida y permitir comentarios

class Pelicula(models.Model):
   nombre = models.CharField(max_length=30)
   director = models.CharField(max_length=20)
   titulo = models.CharField(max_length=30)
   subtitulo = models.CharField(max_length=100)
   opinion = models.TextField()
   puntaje = models.DecimalField(max_digits=3,decimal_places=1)
   fecha = models.DateField()
   #agregar imagen, contemplar idea de autor
   def __str__(self):
       return f'{self.id} - {self.nombre} - {self.puntaje}'

class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=20)
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=100)
    opinion = models.TextField()
    puntaje = models.DecimalField(max_digits=3,decimal_places=1)
    fecha = models.DateField()
    #agregar imagen, contemplar idea de autor
    def __str__(self):
       return f'{self.id} - {self.nombre} - {self.puntaje}'
    
class Cancion(models.Model):
    nombre = models.CharField(max_length=30)
    artista = models.CharField(max_length=20)
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=100)
    opinion = models.TextField()
    puntaje = models.DecimalField(max_digits=3,decimal_places=1)
    fecha = models.DateField()
    #agregar imagen, contemplar idea de autor
    def __str__(self):
       return f'{self.id} - {self.nombre} - {self.puntaje}'
