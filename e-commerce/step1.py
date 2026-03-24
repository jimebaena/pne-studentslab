class Product:
    def __init__(self, name=""):
        self.name = name
    def __str__(self):
        return self.name

product1 = Product("Tomato")
print(product1)
product2 = Product("Tomato")
print(product2)
product3 = Product("Tomato")
print(product3)