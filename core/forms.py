from django.forms import ModelForm
from .models import Resenia

class ReseniaForm(ModelForm):
    class Meta:
        model = Resenia
        fields = ['texto', 'estrellas', 'emailcontacto']
