from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  render(request, "index.html")
    
def computadoras(request):
    return render(request, "computadoras.html")

def cuidado_personal(request):
    return render(request, "cuidado_personal.html")

def deporte(request):
    return render(request, "deporte.html")
    
def electronico(request):
    return render(request, "electronico.html")
    
def hogar(request):
    return render(request, "hogar.html")
    
def indumentaria(request):
    return render(request, "indumentaria.html",)
    
def jardineria(request):
    return render(request, "jardineria.html")
    
def juguetes(request):
    return render(request, "juguetes.html")
    
def mascotas(request):
    return render(request, "mascotas.html")
    
def ofertas(request):
    return render(request, "ofertas.html")
    
def repuestos_autos(request):
    return render(request, "repuestos_autos.html")
        
def videojuegos(request):
    return render(request, "videojuegos.html")
    
def formulario_de_pago(request):
    return render(request, "formulario_de_pago.html")

def indumentaria_con_param(request, cadena):
    return render(request, "indumentaria_con_param.html")
