from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {'username': '',
                      'email':'',
                      'password1':'',
                      'password2':''}
        
class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido',required=False)
    informacion = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name', 'informacion', 'avatar']
        