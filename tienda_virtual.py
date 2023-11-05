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


