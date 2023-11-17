from django import forms
from ckeditor.fields import  RichTextFormField



class BaseFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=200)
    opinion = RichTextFormField()
    puntaje = forms.DecimalField(max_digits=3,decimal_places=1)
    fecha = forms.DateField()
    imagen = forms.ImageField()

class BaseVideojuegoFormulario(BaseFormulario):
    desarrollador = forms.CharField(max_length=20)
    
class BaseCancionFormulario(BaseFormulario):
    artista = forms.CharField(max_length=20)

class BasePeliculaFormulario(BaseFormulario):
    director = forms.CharField(max_length=20)
    
class CrearPelicula(BasePeliculaFormulario):
    ...
    
class ModificarPelicula(BasePeliculaFormulario):
    ...
    
class CrearCancion(BaseCancionFormulario):
    ...
    
class ModificarCancion(BaseCancionFormulario):
    ...   