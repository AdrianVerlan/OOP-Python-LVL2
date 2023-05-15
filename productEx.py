class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    
    def printP(p):
        print("Product:", p.name,"Price:", p.price,"USD")


p1 = Product("OS", 100)
p2 = Product("Antivirus", 140)
p3= Product("Game", 40)

Product.printP(p1)
Product.printP(p2)
Product.printP(p3)