from django.contrib import admin
from .models import Color,Categoria, Stock_item, Destacado_por_categoria, CategoriaAdmin, Stock_itemAdmin

# Register your models here.
admin.site.register(Color)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Stock_item, Stock_itemAdmin)
admin.site.register(Destacado_por_categoria)