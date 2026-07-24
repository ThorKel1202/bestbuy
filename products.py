class Product:
    """
        Class represents a product in the store.
    """
    
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
            Function initializes a product with name, price, and quantity.
            The 'name: str' is the name of the product (must be not empty).
            The 'price: float' is the price of the product (must be non-negative).
            The 'quantity: int' is the available quantity (must be non-negative).
            It raises the following errors:
            ValueError: If name is empty, or price/quantity is negative.
        """
        
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
        """
            Function returns the current quantity of the product.
        """
        
        return self.quantity
    
    def set_quantity(self, quantity: int) -> None:
        """
            Function sets a new quantity for the product. If quantity
            becomes 0, the product is deactivated.
            The 'quantity: int' is the new quantity value.
            It raises the following errors:
            ValueError: If quantity is negative.
        """
        
        if quantity < 0:
            raise ValueError("Quantity must be positive!")
        
        self.quantity = quantity
        
        # Call deactivate() if quantity is 0 to set "activ" on False
        if self.quantity == 0:
            self.deactivate()
    
    def is_active(self) -> bool:
        """
            Function returns True if the product is active.
        """
        
        return self.active
    
    def activate(self) -> None:
        """
            Function activates the product.
        """
        
        self.active = True
    
    def deactivate(self) -> None:
        """
            Function deactivates the product.
        """
        
        self.active = False
    
    def show(self) -> None:
        """
            Function prints product details.
        """
        
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")
    
    def buy(self, quantity: int) -> float:
        """
            Function purchases a given quantity of the product.
            As well, it reduces the available quantity and deactivates the
            product if it reaches 0. The 'quantity:' is the amount of items to buy.
            It returns the total price of the purchase.
            It raises the following errors:
            ValueError: If quantity is not positive.
            RuntimeError: If product is inactive
            ValueError: If product has insufficient stock.
        """
        
        if quantity <= 0:
            raise ValueError("Amount must be more than 0 (zero)!")
        
        if not self.active:
            raise RuntimeError("Product is not active!")
        
        if quantity > self.quantity:
            raise ValueError("Insufficient stock available!")
        
        # Reduce quantity after buy
        self.quantity -= quantity
        
        # Call deactivate() if quantity is 0 to set "activ" on False
        if self.quantity == 0:
            self.deactivate()
        
        # Total payment
        return quantity * self.price
    
