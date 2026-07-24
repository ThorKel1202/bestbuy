class Product:
    def __init__(self, name, price, quantity):
        
        # Validate the input
        if not name:
            raise ValueError("Name can not be empty!")
        if price < 0:
            raise ValueError("Price can not be negative!")
        if quantity < 0:
            raise ValueError("Quantity can not be negative!")
        
        # Create the instance
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be positive!")
        
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
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")
    
    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Amount must be more than 0 (zero)!")
        
        if not self.active:
            raise Exception("Product is not active!")
        
        if quantity > self.quantity:
            raise Exception("Insufficient stock available!")
        
        # Reduce quantity after buy
        self.quantity -= quantity
        
        # Call deactivate() if quantity is 0 to set "activ" on False
        if self.quantity == 0:
            self.deactivate()
        
        # Total payment
        return quantity * self.price
    
