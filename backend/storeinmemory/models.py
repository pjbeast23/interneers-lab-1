class Product:
    id_counter = 1
    
    def __init__(self, name, description, category, price, brand, quantity):
        self.id = Product.id_counter
        Product.id_counter += 1
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.brand = brand
        self.quantity = quantity

