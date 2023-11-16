from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login

from accounts.forms import FormularioCreacion, EdicionPerfil
from accounts.models import DatosExtra 

def login(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            
            django_login(request,user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('lobby')
        else:
            return render(request, 'accounts/login.html', {'formulario_login': formulario})
    
    formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario_login': formulario})

def registro(request):
    formulario = FormularioCreacion()
    
    if request.method == "POST":
        formulario = FormularioCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
        
    
    return render(request, 'accounts/registro.html', {"formulario_registro" : formulario})

def perfil(request):
    
    return render(request, 'accounts/perfil.html', {})

def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = EdicionPerfil(initial = {'informacion': datos_extra.informacion, 'avatar': datos_extra.avatar},instance=request.user)
    
    if request.method == "POST":
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data.get('informacion')
            avatar = formulario.cleaned_data.get('avatar')
            
            if informacion:
                datos_extra.informacion = informacion
            if avatar:
                datos_extra.avatar = avatar
            
            datos_extra.save()    
            formulario.save()
            
            return redirect('lobby')
    
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'accounts/cambiar_password.html'
    success_url = reverse_lazy('perfil')
    
    