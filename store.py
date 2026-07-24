from typing import List
from products import Product


class Store:
    """
        Represents a store that manages a collection of products.
    """
    
    def __init__(self, products: List[Product]) -> None:
        """
            Function initializes the store with a list of products.
            The 'products: List[Product]' is the Initial list of products
            in the store.
        """
        
        self.products = products


    def add_product(self, product: Product) -> None:
        """
            Function adds a product to the store.
            The 'product: Product' is the product to add.
        """
        
        self.products.append(product)


    def remove_product(self, product: Product) -> None:
        """
            Function removes a product from the store if it exists.
            The 'product: Product' is the product to remove.
        """
        
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        """
            function returns the total quantity of all products in the store.
        """
        
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> List[Product]:
        """
            Function returns a list of all active products in the store.
        """
        
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list: List[tuple[Product, int]]) -> float:
        """
            Function processes an order and return the total price.
            The shopping_list is a list of tuples containing a product and quantity.
            It returns the total price of the order.
        """
        
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
