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

if __name__ == "__main__":
    store = Store()
    """store.add_product("Camisa", 5000, 50)"""

    while True:
        #ciclo que permite mostrar el menú de opciones
        print("Options:")
        print("1. Add a product")
        print("2. List products")
        print("3. Purchase a product")
        print("4. Check inventory")
        print("5. Quit")
        
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            stock = int(input("Enter the product stock: "))
            store.add_product(name, price, stock)
            print("Product added.")
        elif choice == "2":
            products = store.list_products()
            print("Products:")
            for product in products:
                print(product)
        elif choice == "3":
            name = input("Enter the product name you want to purchase: ")
            quantity = int(input(f"Enter the quantity of {name} you want to purchase: "))
            result = store.purchase_product(name, quantity)
            print(result)
        elif choice == "4":
            inventory = store.check_inventory()
            print("Inventory:")
            for item in inventory:
                print(item)
        elif choice == "5":
            # Save purchase history to a file
            with open("purchase_history.txt", "w") as file:
                for item in store.purchase_history:
                    file.write(f"Product: {item[0]}, Quantity: {item[1]}, Total: ${item[2]}\n")
            print("Purchase history saved to 'purchase_history.txt'.")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")


        
    


