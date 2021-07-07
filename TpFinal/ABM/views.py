from django.contrib.auth.models import User
from django.db.models import query
from django.db.models.query_utils import Q
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django import forms
from django.utils import html
from django.urls import reverse
from .models import Categoria, Producto
from .forms import *

##Productos = ["Libro", "Lapiz", "Goma"]
class FormAltaProducto(forms.Form):
    Producto = forms.CharField(label="Nuevo Producto")


def  acerca(request):
    return render(request, "productos/AcercaDe.html")

def index(request):
    querySet = request.GET.get("buscar")
    principales = Producto.objects.all().order_by("-id")[0:3]
    productos = Producto.objects.all().order_by("-id")[3:10]
    if querySet:
        productos = Producto.objects.filter(
            Q(nombre__icontains = querySet),
            Q(precio__icontains = querySet)

        ).distinct()
    return render(request, "productos/index.html", {"productos":productos, "principales":principales })

    

def productos(request):
    if "Productos" not in request.session:
        request.session["Productos"]=[]
    return render(request, "productos/productos.html", {
        "lista_productos": Producto.objects.all()
        #'Productos': request.session["Productos"]
        })

def categorias(request):
    if "categorias" not in request.session:
        request.session["categorias"]=[]
    return render(request, "productos/layout.html", {
        "lista_categoria": Categoria.objects.all()

        })

def agregar(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormProducto(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen']))
        if form.is_valid():
            form.save()
        return redirect("ABM:index")          
    else:
        form = FormProducto()
        return render(request, "productos/agregar.html", {
        "form":form
        })

def editar(request, producto_id):
        un_producto = Producto.objects.filter(id=producto_id).first()
        if request.method == "POST":  
            user = User.objects.get(username=request.user)   
            form = FormProducto(data=request.POST, instance=un_producto)
            if form.is_valid():
                form.save()
            return redirect("ABM:productos")
        else:
                form = FormProducto(instance = un_producto)
                return render(request, 'productos/editar.html', {
                "form": form,
                "un_producto": un_producto
                
        })

def eliminar(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    un_producto.delete()
    return redirect("ABM:productos")



def productosver(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "productos/productosver.html", {
        "producto": un_producto
    })

def categoriasFiltro(request, producto_categoria):
    
    productos = Producto.objects.filter(categoria=producto_categoria)
    return render(request, "productos/categorias.html", {
        "productos": productos
    })


def buscar(request):

    queryset = request.GET.get("buscar")
    if queryset:
        productos = Producto.objects.filter(
            Q(titulo__icontains = queryset)
        ).distinct()

        data = {
            'productos':productos
        }
        return render(request, 'productos/busqueda.html',data)
    else:
        return render(request, "productos/busqueda.html",{})