from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.http import HttpResponse


def login(request):
    
    if request.method == "GET":
        print("Enviando formulario!")
        
        return render(request, "core/login.html",{
        "form": UserCreationForm 
    })
        
    else:
        if request.POST["password1"] == request.POST["password1"]:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
            user.save()
            return HttpResponse("Usuario creado!")
        return HttpResponse("La contraseña no coincide!")
             
       
    
 
    


def index(request):
    return  render(request, "core/index.html")
    
def computadoras(request):
    return render(request, "core/computadoras.html")

def cuidado_personal(request):
    return render(request, "core/cuidado_personal.html")

def deporte(request):
    return render(request, "core/deporte.html")
    
def electronico(request):
    return render(request, "core/electronico.html")
    
def hogar(request):
    return render(request, "core/hogar.html")
    
def indumentaria(request):
    return render(request, "core/indumentaria.html")
    
def jardineria(request):
    return render(request, "core/jardineria.html")
    
def juguetes(request):
    return render(request, "core/juguetes.html")
    
def mascotas(request):
    return render(request, "core/mascotas.html")
    
def ofertas(request):
    return render(request, "core/ofertas.html")
    
def repuestos_autos(request):
    return render(request, "core/repuestos_autos.html")
    
    
def videojuegos(request):
    return render(request, "core/videojuegos.html")
    
def formulario_de_pago(request):
    return render(request, "core/formulario_de_pago.html")
    