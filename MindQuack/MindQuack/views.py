from django.http import HttpResponse
from django.template import Template,Context
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render,redirect

def main(request):
    
    documentoExterno=open("C:/Users/FaliLeal11/Desktop/uni/UNI-3/SSIpython/MindQuack/MindQuack/Template/main.html")
    plantilla=Template(documentoExterno.read())
    documentoExterno.close()
    contexto=Context()
    man=plantilla.render(contexto)

    return HttpResponse (man)

'''
def register(request):
    form= UserChangeForm()

    if request.method == 'POST':
        form=UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'C:/Users/FaliLeal11/Desktop/uni/UNI-3/SSIpython/MindQuack/MindQuack/plantilla/reg.html',context)
'''
