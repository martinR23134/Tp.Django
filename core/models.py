from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

# Create your models here.
class Color(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Stock_item(models.Model):
    # COLORES = [
    #     ('B', 'Blanco'),
    #     ('N', 'Negro'),
    #     ('A', 'Azul'),
    # ]
    nombre = models.CharField(max_length=100)
    foto =  models.ImageField(upload_to = 'imgs/')
    categorias = models.ManyToManyField(Categoria, through='Destacado_por_categoria')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
            # Precio máximo de 8 cifras (del orden de 100 millones)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True)
#    color = models.CharField(max_length=1, choices=COLORES, null=True)
    descripcion = models.TextField(max_length=500, null=True)
        # If you specify a max_length attribute, it will be reflected in the Textarea widget 
        # of the auto-generated form field. However it is not enforced at the model or database level. 
        # Use a CharField for that.
    info_adicional = models.TextField(max_length=500, null=True)
#   reseñas = ...
#   productos_relacionados = ...
    def __str__(self):
        return self.nombre

class Destacado_por_categoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    stock_item = models.ForeignKey(Stock_item, on_delete=models.PROTECT, null=True)
    destacado = models.BooleanField(null=True)

class Destacado_por_categoria_inline(admin.TabularInline):
    model = Destacado_por_categoria
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    inlines = (Destacado_por_categoria_inline,)

class Stock_itemAdmin(admin.ModelAdmin):
    inlines = (Destacado_por_categoria_inline,)

def validate_no_unt(cadena):
    if 'unt' in cadena.lower():
        raise ValidationError('No se aceptan emails referidos a UNT')

class Resenia(models.Model):
    ESTRELLAS_CHOICES = [
        (1, 'Una estrella'),
        (2, 'Dos estrellas'),
        (3, 'Tres estrellas'),
        (4, 'Cuatro estrellas'),
        (5, 'Cinco estrellas'),
    ]
    texto = models.TextField(max_length=500, null=True)
    estrellas = models.IntegerField(choices=ESTRELLAS_CHOICES, null=True)
    emailcontacto = models.EmailField(null=True, validators=[validate_no_unt])
    item_reseniado = models.ForeignKey(Stock_item, on_delete=models.PROTECT, null=True)
