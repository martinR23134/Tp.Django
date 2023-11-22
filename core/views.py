import json
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Categoria, Stock_item, Destacado_por_categoria, Resenia
from .forms import ReseniaForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


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

def destacado_y_relacionados_por_nro_categoria(request, nro):
    contexto = None
    categoria_del_nro = Categoria.objects.get(pk=nro)  # Esto es un obj Categoria, salvo Exception
    destacado_del_nro = Destacado_por_categoria.objects.get(categoria=categoria_del_nro, destacado=True)
    item_destacado=destacado_del_nro.stock_item
    items_relacionados_con_destacado = Stock_item.objects.filter(categorias=categoria_del_nro)
    items_relacionados=items_relacionados_con_destacado.exclude(pk=item_destacado.pk)
    contexto = { "item_destacado": item_destacado, #item_destacado es un objeto Stock_item
                "items_relacionados": items_relacionados, #items_relacionados es un queryset
                "cat": categoria_del_nro # categoria_del_string es un objeto Categoria
                }
    return render(request, "core/destacado_y_relac_x_bd.html", context=contexto)

def destacado_y_relacionados_por_string_categoria(request, string_categoria):
    contexto = None
    categoria_del_string = Categoria.objects.get(nombre=string_categoria)  # Esto es un obj Categoria, salvo Exception
    destacado_del_string = Destacado_por_categoria.objects.get(categoria_id=categoria_del_string.pk, destacado=True)
    item_destacado=destacado_del_string.stock_item
    items_relacionados_con_destacado = Stock_item.objects.filter(categorias=categoria_del_string)
    items_relacionados=items_relacionados_con_destacado.exclude(pk=item_destacado.pk)
    contexto = { "item_destacado": item_destacado, #item_destacado es un objeto Stock_item
                "items_relacionados": items_relacionados, #items_relacionados es un queryset
                "cat": categoria_del_string # categoria_del_string es un objeto Categoria
                }
    return render(request, "core/destacado_y_relac_x_bd.html", context=contexto)

# class ReseniaFormView(View):
#     form_class = ReseniaForm
#     initial = { 'texto':'',
#                 'estrellas':'',
#                 'emailcontacto':''  
#               }
#     template_name = 'core/formulario_resenia.html'
#     def get(self, request):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()            
# #            string_categoria='Auriculares'
# #            return HttpResponseRedirect(reverse('core:destacado_y_relac_x_bd', args=(string_categoria)))
#             return HttpResponseRedirect(reverse('index'))
#         return render(request, self.template_name, {'form': form})
    
class ReseniaFormView(LoginRequiredMixin, View):
    login_url = '/admin/login/'
#    redirect_field_name = 'redirect_to'
    form_class = ReseniaForm
    initial = { 'texto':'',
                'estrellas':'',
                'emailcontacto':''  
              }
    template_name = 'core/formulario_resenia.html'
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()            
#            string_categoria='Auriculares'
#            return HttpResponseRedirect(reverse('core:destacado_y_relac_x_bd', args=(string_categoria)))
            return HttpResponseRedirect(reverse('index'))
        return render(request, self.template_name, {'form': form})
