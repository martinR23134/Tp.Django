import json
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def login(request):

    if request.method == "GET":
        print("Enviando formulario!")

        return render(request, "core/login.html", {
            "form": UserCreationForm
        })

    else:
        if request.POST["password1"] == request.POST["password1"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            user.save()
            return HttpResponse("Usuario creado!")
        return HttpResponse("La contraseña no coincide!")


def index(request):
    return render(request, "core/index.html")


def computadoras(request, computadora_id=None):

    # SIMULAMOS UNA BD
    producto_lista = [
        {
            "id": 1,
            "nombre": "Notebook Lenovo Ideapad 1i Intel I3 1215u 4gb Ram.",
            "precio": 235.99,
            "marca": "Lenovo",
            "pulgadas_pantalla": 15.6,
            "procesador": "Intel Core I3",
            "memoria_ram": "4GB Ram",
            "almacenamiento": "256GB SSD",
            "detalles": "La notebook LENOVO 82QC003VUS es una solución tanto para trabajar y, estudiar como para entretenerte. Al ser portátil, el escritorio dejará de ser tu único espacio de uso para abrirte las puertas a otros ambientes ya sea en tu casa o en la oficina. <br><br> Eficiencia a tu alcance <br> Su procesador Intel Core i3 de 12.ª generación, está pensado para aquellas personas generadoras y consumidoras de contenidos. Con esta unidad central, la máquina llevará a cabo varios procesos de forma simultánea, desde edición de videos hasta retoques fotográficos con programas profesionales",
            "img": "core/img/D_NQ_NP_787180-MLA54518190876_032023-O.jpg"
        },
        {
            "id": 2,
            "nombre": 'Notebook HP 15-ef2514la plata 15.6", AMD Ryzen 7 5700U 8GB',
            "precio": 125.99,
            "marca": "HP",
            "pulgadas_pantalla": 15.6,
            "procesador": "Intel Core i7",
            "memoria_ram": "8GB",
            "almacenamiento": "512GB SSD",
            "detalles": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae laborum ad provident omnis expedita ipsam quod natus nostrum, aspernatur facilis laudantium sequi et illo eos ducimus minima sit mollitia amet ipsa suscipit doloribus temporibus nobis quasi.<br><br> Illo facilis alias at quos sed perferendis sapiente rerum error porro, voluptates nam aut debitis perspiciatis iure provident quis expedita eius voluptate fugit eos.",
            "img": "core/img/D_NQ_NP_982323-MLA51606812711_092022-O.jpg"
        },
        {
            "id": 3,
            "nombre": 'Notebook Lenovo Ideapad Core I3-1215u 8gb 256gb',
            "precio": 157.99,
            "marca": "Lenovo",
            "pulgadas_pantalla": 13.3,
            "procesador": "Intel Core i3",
            "memoria_ram": "8GB",
            "almacenamiento": "256GB SSD",
            "detalles": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae laborum ad provident omnis expedita ipsam quod natus nostrum, aspernatur facilis laudantium sequi et illo eos ducimus minima sit mollitia amet ipsa suscipit doloribus temporibus nobis quasi.<br><br> Illo facilis alias at quos sed perferendis sapiente rerum error porro, voluptates nam aut debitis perspiciatis iure provident quis expedita eius voluptate fugit eos.",
            "img": "core/img/D_NQ_NP_891677-MLA54927903010_042023-O.jpg"
        },
        {
            "id": 4,
            "nombre": 'Notebook Lenovo V-Series V15-G2-ITL iron gray 15.6"',
            "precio": 213.99,
            "marca": "Lenovo",
            "pulgadas_pantalla": 15.6,
            "procesador": "Intel Core i5",
            "memoria_ram": "8GB",
            "almacenamiento": "512GB SSD",
            "detalles": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae laborum ad provident omnis expedita ipsam quod natus nostrum, aspernatur facilis laudantium sequi et illo eos ducimus minima sit mollitia amet ipsa suscipit doloribus temporibus nobis quasi.<br><br> Illo facilis alias at quos sed perferendis sapiente rerum error porro, voluptates nam aut debitis perspiciatis iure provident quis expedita eius voluptate fugit eos.",
            "img": "core/img/D_NQ_NP_745797-MLA69340654813_052023-O.jpg"
        },
        {
            "id": 5,
            "nombre": 'Notebook Lenovo IdeaPad 15ITL6 arctic gray 15.6", Intel Core i7',
            "precio": 176.99,
            "marca": "Lenovo",
            "pulgadas_pantalla": 15.6,
            "procesador": "Intel Core i7",
            "memoria_ram": "16GB",
            "almacenamiento": "512GB SSD",
            "detalles": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae laborum ad provident omnis expedita ipsam quod natus nostrum, aspernatur facilis laudantium sequi et illo eos ducimus minima sit mollitia amet ipsa suscipit doloribus temporibus nobis quasi.<br><br> Illo facilis alias at quos sed perferendis sapiente rerum error porro, voluptates nam aut debitis perspiciatis iure provident quis expedita eius voluptate fugit eos.",
            "img": "core/img/D_NQ_NP_916089-MLA52855783526_122022-V.jpg"
        }
    ]

    try:
        notebook_encontrada = None
        for data in producto_lista:
            if data['id'] == computadora_id:
                notebook_encontrada = data
                break

    except ValueError as err:
        print(err)

    print(notebook_encontrada)
    return render(request, "core/computadoras.html", {"context": notebook_encontrada})


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
