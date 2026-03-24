class Product:
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price
    def __str__(self):
        return self.name, self.price

p1 = Product("Laptop", 1200)
name1 = p1.name
price1 = p1.price
print(f"{name1}: {price1}")

p2 = Product("Chair", 90)
name2 = p2.name
price2 = p2.price
print(f"{name2}: {price2}")

p3 = Product("Scarf", 24)
name3 = p3.name
price3 = p3.price
print(f"{name3}: {price3}")