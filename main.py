import products
import store
import sys


def list_products(best_buy: store.Store) -> None:
    """
        The function prints all active products available in the store.
        The "best_buy" gets all active products. It's the
        store instance containing products.
    """
    
    all_products = best_buy.get_all_products()
    print("------")
    for i, product in enumerate(all_products):
        print(f"{i + 1}. ", end="")
        product.show()
    print("------")


def show_total(best_buy: store.Store) -> None:
    """
        Function displays the total quantity of all products in the store.
        The "best_buy" gets the total quantity. It's the store instance.
    """
    
    total = best_buy.get_total_quantity()
    print("------")
    print(f"Total amount in store: ${total}")
    print("------")


def make_order(best_buy: store.Store) -> None:
    """
        Function asks user to create an order and print the total price.
        It prompts the user to select products and quantities, then processes
        the order using the store. The "best_buy" gets all active products and order.
        It's the store instance containing products and order.
    """
    
    all_products = best_buy.get_all_products()

    print("------")
    for i, product in enumerate(all_products):
        print(f"{i + 1}. ", end="")
        product.show()
    print("------")

    shopping_list = []

    print("When you want to finish order, enter empty text.")
    while True:
        product_input = input("Which product # do you want? ")
        if product_input == "":
            break

        quantity_input = input("What amount do you want? ")

        try:
            product_index = int(product_input) - 1
            quantity = int(quantity_input)

            selected_product = all_products[product_index]
            shopping_list.append((selected_product, quantity))
            print("Product added to list!\n")

        except (ValueError, IndexError):
            print("Error adding product!\n")

    try:
        total_price = best_buy.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price}")
        
    except ValueError:
        print("Invalid input!")
    
    except Exception:
        print("Order failed.")


def quit_program(_: store.Store) -> None:
    """
        Function ends the application.
        """
    
    sys.exit()
    

def start(best_buy: store.Store) -> None:
    """
        Function starts the interactive store menu. Displays a menu
        and dispatches user choices to the correct functions.
        The "best_buy" is the store instance to interact with.
    """
    
    dispatcher = {
        "1": list_products,
        "2": show_total,
        "3": make_order,
        "4": quit_program,
    }

    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        action = dispatcher.get(choice)

        if action:
            action(best_buy)
        else:
            print("Invalid option, please choose again.")
    

def main() -> None:
    """
        Function initializes the store and start the application.
    """
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
