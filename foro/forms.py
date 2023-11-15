from django import forms

class BaseVideojuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    desarrollador = forms.CharField(max_length=20)
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=100)
    opinion = forms.CharField(max_length=250)
    puntaje = forms.DecimalField(max_digits=3,decimal_places=1)
    fecha = forms.DateField()

class BaseCancionFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    artista = forms.CharField(max_length=20)
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=100)
    opinion = forms.CharField(max_length=250)
    puntaje = forms.DecimalField(max_digits=3,decimal_places=1)
    fecha = forms.DateField()

class CrearVideojuego(BaseVideojuegoFormulario):
    ...
    
class ModificarVideojuego(BaseVideojuegoFormulario):
    ...
    
class CrearCancion(BaseCancionFormulario):
    ...
    
class ModificarCancion(BaseCancionFormulario):
    ...   