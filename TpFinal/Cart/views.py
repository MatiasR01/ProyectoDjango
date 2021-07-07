from django.shortcuts import render

# Create your views here.
from .cart import Cart

from .models import Producto
from django.shortcuts import redirect

def  agregar(request, producto_id):
    cart = Cart(request)

    producto = Producto.objects.get(id=producto_id)
    cart.add(producto=producto)

    return redirect("ABM:index")

def  eliminar(request, producto_id):
    cart = Cart(request)

    producto = Producto.objects.get(id=producto_id)
    cart.remove(producto=producto)

    return redirect("ABM:index")    

def  restar(request, producto_id):
    cart = Cart(request)

    producto = Producto.objects.get(id=producto_id)
    cart.decrement(producto=producto)

    return redirect("ABM:index")  

def  limpiar(request, producto_id):
    cart = Cart(request)

    cart.clear()

    return redirect("ABM:index")  
    



