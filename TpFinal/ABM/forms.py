from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('titulo', 'descripcion', 'precio','categoria', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'pub_descripcion'}),
            'precio': forms.TextInput(attrs={'class': 'pub_precio'}),
            'categoria': forms.Select(attrs={'class': 'pub_categoria'}),
            'imagen': forms.FileInput(attrs={'name':'imagen', 'class': 'pub_imagen'}),
        }

