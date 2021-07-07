from .models import Categoria

def categoriastraer(request):

    cate = Categoria.objects.values_list("categoria", flat=True)
    return {
        'lista_categoria': cate
    }