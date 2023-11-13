from django.db import models
from django.core.validators import MaxValueValidator

# idea es crear foro donde opinen sobro media consumida y permitir comentarios

class Pelicula(models.Model):
   nombre = models.CharField(max_length=30)
   director = models.CharField(max_length=20)
   titulo = models.CharField(max_length=30)
   opinion = models.TextField()
   puntaje = models.DecimalField(max_digits=2,decimal_places=1,validators=[MaxValueValidator(10)])
   #agregar imagen y fecha, contemplar idea de autor

class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=20)
    titulo = models.CharField(max_length=30)
    opinion = models.TextField()
    puntaje = models.DecimalField(max_digits=2,decimal_places=1,validators=[MaxValueValidator(10)])
    #agregar imagen y fecha, contemplar idea de autor
    
class Cancion(models.Model):
    nombre = models.CharField(max_length=30)
    artista = models.CharField(max_length=20)
    titulo = models.CharField(max_length=30)
    opinion = models.TextField()
    puntaje = models.DecimalField(max_digits=2,decimal_places=1,validators=[MaxValueValidator(10)])
    #agregar imagen y fecha, contemplar idea de autor
