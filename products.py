class Product:
    def __init__(self, name, price, quantity):
        
        # Validate the input
        if not name:
            raise ValueError("Name darf nicht leer sein.")
        if price < 0:
            raise ValueError("Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        
        # Create the instance
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        
        self.quantity = quantity
        
        # Call deactivate() if quantity is 0 to set "activ" on False
        if self.quantity == 0:
            self.deactivate()
    
    def is_active(self) -> bool:
        return self.active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")
    
    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")
        
        if not self.active:
            raise Exception("Produkt ist nicht aktiv.")
        
        if quantity > self.quantity:
            raise Exception("Nicht genügend Bestand vorhanden.")
        
        # Reduce quantity after buy
        self.quantity -= quantity
        
        # Call deactivate() if quantity is 0 to set "activ" on False
        if self.quantity == 0:
            self.deactivate()
        
        # Total payment
        return quantity * self.price
    
def main():
    
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
    
if __name__ == "__main__":
    main()
    
    