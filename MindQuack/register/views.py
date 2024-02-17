from django.http import request,response
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.template import Template,Context
# Create your views here.

def login(request):
    documentoExterno=open("register/template/login.html")
    plantilla=Template(documentoExterno.read())
    documentoExterno.close()
    contexto=Context()
    man=plantilla.render(contexto)

    return HttpResponse (man)

def register(request):
    context ={}
    return render( request , "template/register.html" )

#Futuro uso para el perfil de los usuarios
def Profile(request):
    NameUser = Usuarios.objects.all() 
    return render(request, 'template/profile.html', {'NameUser' : NameUser})
