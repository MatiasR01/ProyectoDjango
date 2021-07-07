from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=64, primary_key=True)
    descripcion = models.CharField(max_length=64)
    def  __str__(self):
        return f"{self.categoria} {self.descripcion}"

class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=1200)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name="fk_cate")
    imagen = models.ImageField(upload_to="productos")

    def  __str__(self):
        return f"Producto #{self.id}: {self.titulo} descripcion: {self.descripcion} Precio: {self.precio} Categoria: {self.categoria}"
        


class Carrito(models.Model):
    usuario = models.CharField(max_length=64)
    lista = models.CharField(max_length=64)
    total = models.IntegerField()
    def  __str__(self):
        return f"{self.usuario} {self.lista} {self.total}"