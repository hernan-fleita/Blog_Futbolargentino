import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date
from .models import Boca,River,Sanlorenzo
from Appdivsion1.forms import BocaFormulario,RiverFormulario,SanlorenzoFormulario
# Create your views here.

def inicio(request):
    return render(request, "Appdivsion1/inicio.html")




def boca(request):  
    if request.method=="POST":
        miformulario= BocaFormulario(request.POST)
  
        if miformulario.is_valid():
            info=miformulario.cleaned_data  
            bocaj=Boca(nombre=info["nombre"], goles=info["goles"]) 
            bocaj.save()
            return render(request, "Appdivsion1/inicio.html",{"mensaje": "nombre creado"})
        else:
            return render(request, "Appdivsion1/inicio.html",{"mensaje": "Error"})
    else:
        miformulario=BocaFormulario()
    return render(request, "Appdivsion1/boca.html", {"formulario":miformulario})




 

def sanlorenzo(request):  
    if request.method=="POST":
        miformulario= SanlorenzoFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid():
            info=miformulario.cleaned_data
           
            casla=Sanlorenzo(nombre=info["nombre"],goles=info["goles"])
            casla.save()
            return render(request, "Appdivsion1/inicio.html",{"mensaje": "nombre creado"})
        else:
            return render(request, "Appdivsion1/inicio.html",{"mensaje": "Error"})
    else:
        miformulario=SanlorenzoFormulario()
    return render(request, "Appdivsion1/sanlorenzo.html", {"formulario":miformulario}) 

def river(request):  
    if request.method=="POST":
        miformulario= RiverFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid():
            info=miformulario.cleaned_data
           
            carp=River(nombre=info["nombre"],goles=info["goles"])
            carp.save()
            return render(request, "Appdivsion1/inicio.html",{"mensaje": "nombre creado"})
        else:
            return render(request, "Appdivsion1/inicio.html",{"mensaje": "Error"})
    else:
        miformulario=RiverFormulario()
    return render(request, "Appdivsion1/river.html", {"formulario":miformulario}) 


def busquedaboca(request):  
    return render(request, "Appdivsion1/busquedaboca.html")


def buscarboca(request):
    if request.GET["goles"]:
        nom=request.GET["goles"]
        gl=Boca.objects.filter(goles=nom)
        if len(gl)!=0:
         return render(request, "Appdivsion1/resultadobusqueda.html", {"goles":gl})
        else:
            return render(request, "Appdivsion1/resultadobusqueda.html", {"mensaje":"no hay GOLES"})
   
    else:
        return render(request, "Appdivsion1/resultadobusqueda.html", {"mensaje":"no enviaste datos!!!"})