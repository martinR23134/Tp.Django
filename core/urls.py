from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("computadoras/", views.computadoras, name="computadoras"),
    path("computadoras/<int:computadora_id>", views.computadoras, name="computadoras"),
    path("cuidado_personal/", views.cuidado_personal, name="cuidado_personal"),
    path("deporte/", views.deporte, name="deporte"),
    path("electronico/", views.electronico, name="electronico"),
    path("hogar/", views.hogar, name="hogar"),
    path("indumentaria/", views.indumentaria, name="indumentaria"),
    path("jardineria/", views.jardineria, name="jardineria"),
    path("juguetes/", views.juguetes, name="juguetes"),
    path("mascotas/", views.mascotas, name="mascotas"),
    path("ofertas/", views.ofertas, name="ofertas"),
    path("mascotas/", views.mascotas, name="mascotas"),
    path("repuestos_autos/", views.repuestos_autos, name="repuestos_autos"),
    path("videojuegos/", views.videojuegos, name="videojuegos"),
    path("formulario_de_pago/", views.formulario_de_pago, name="formulario_de_pago"),
    path("login/", views.login, name="login"),
    path("destacado_y_relac_x_bd/<int:nro>/", views.destacado_y_relacionados_por_nro_categoria, name="destacado_y_relacionados_por_nro_categoria"),
    path("destacado_y_relac_x_bd/<str:string_categoria>/", views.destacado_y_relacionados_por_string_categoria, name="destacado_y_relacionados_por_string_categoria"),
    path("formulario_resenia/", views.ReseniaFormView.as_view(), name="formulario_resenia"),
]
