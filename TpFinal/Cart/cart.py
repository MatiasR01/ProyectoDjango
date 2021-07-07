class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def  add(self, producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id":producto.id,
                "titulo":producto.titulo,
                "quantitu":1,
                "price": str(producto.price),
                "image": producto.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["quantity"] = value["quantity"] + 1
                    
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    def decrement(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value["quantity"] = value ["quantity"] + 1
                if value["quantity"] < 1:
                    self.remove(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    def clear(self):
        self.session["cart"] = {}
        self.session,modified = True