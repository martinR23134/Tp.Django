from django.db import models
from django.contrib import admin

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Stock_item(models.Model):
    COLORES = [
        ('B', 'Blanco'),
        ('N', 'Negro'),
        ('A', 'Azul'),
    ]
    nombre = models.CharField(max_length=100)
    foto =  models.ImageField(upload_to = 'imgs/')
    categorias = models.ManyToManyField(Categoria, through='Destacado_por_categoria')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
            # Precio máximo de 8 cifras (del orden de 100 millones)
#    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True)
    color = models.CharField(max_length=1, choices=COLORES, null=True)
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