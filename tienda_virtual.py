class Product:
    """Clase que representa un producto en general."""
    def __init__(self, name, price, stock):
        """Constructor de la clase Product."""
        self.name = name
        self.price = price
        self.stock = stock

class Store:
    """Clase que representa una tienda en general."""
    def __init__(self):
        """Constructor de la clase Store."""
        self.products = []
        self.purchase_history = []
        
    def add_product(self, name, price, stock):
        """Método que permite agregar un producto a la tienda."""
        product = Product(name, price, stock)
        self.products.append(product)
        
    def list_products(self):
        """Método que permite listar los productos de la tienda."""
        return [f"{product.name} - Price: ${product.price} - Stock: {product.stock}" for product in self.products]
    
    
    def purchase_product(self, name, quantity):
        """Método que permite comprar un producto de la tienda."""
        product = next((p for p in self.products if p.name.lower() == name.lower()), None)
        
        if product and product.stock >= quantity:
            product.stock -= quantity
            purchase_total = product.price * quantity
            self.purchase_history.append((product.name, quantity, purchase_total))
            return f"You purchased {quantity} {product.name}(s) for ${purchase_total}."
        elif product and product.stock < quantity:
            return f"Sorry, only {product.stock} {product.name}(s) available."
        else:
            return "Product not found."
    
    def check_inventory(self):
        """Método que permite revisar el inventario de la tienda."""
        return [f"{product.name} - Stock: {product.stock}" for product in self.products]

        
    


