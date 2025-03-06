# Creating superclass Grocery Item
class GroceryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Creating superclass Shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    # Method to add item
    def add_item(self, item, quantity):
        if quantity <= 0:
            print("Quantity must be a positive number.")
            return

        if item.name in self.cart:
            self.cart[item.name]["quantity"] += quantity
        else:
            self.cart[item.name] = {"price": item.price, "quantity": quantity}
        print(f"{quantity} of {item.name} added to cart.")
        

    # Method to remove item
    def remove_item(self, item_name):
        if item_name in self.cart:
            del self.cart[item_name]
            print(f"{item_name} removed from the cart.")
        else:
            print(f"{item_name} is not in the cart.")


    # Method to view cart
    def view_cart(self):
        print("\nYour shopping cart:")
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = 0
            for item_name, details in self.cart.items():
                item_total = details["price"] * details["quantity"]
                total += item_total
                print(f"{item_name}: Rs {details['price']:.2f} X {details['quantity']} = Rs {item_total:.2f}")
            print(f"Total: Rs {total:.2f}")


    # Method to print receipt
    def print_receipt(self):
        print("\n------ Receipt ------")
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = 0
            for item_name, details in self.cart.items():
                item_total = details["price"] * details["quantity"]
                total += item_total
                print(f"{item_name.capitalize()}: Rs {details['price']:.2f} X {details['quantity']} = Rs {item_total:.2f}")
            print("-" * 30)
            print(f"Total: Rs {total:.2f}")
            print("Thank you for shopping with us!")
        print("-" * 30)


# Creating subclass Grocery management to inherit from class ShoppingCart
class GroceryManagement(ShoppingCart):
    def __init__(self):
        super().__init__()  # Initialize the ShoppingCart
        self.items = {
            "apple": GroceryItem("Apple", 3.00),
            "milk": GroceryItem("Milk", 173.00)
        }

    # Method to create a user interface and show options available
    def show_option(self):
        print("\nGrocery Management System:")
        print("1. View available items")
        print("2. Add items to cart")
        print("3. Remove item from the cart")
        print("4. View cart")
        print("5. Print receipt")
        print("6. Exit")

    # Methods to view items available in the store
    def view_items(self):
        print("\nAvailable Items:")
        for item_name, item in self.items.items():
            print(f"{item_name.capitalize()}: Rs {item.price:.2f}")

    # Method to add item(s) to cart
    def add_items_to_cart(self):
        item_name = input("Enter the item name to add to cart: ").strip().lower()
        if item_name in self.items:
            try:
                quantity = int(input("Enter the quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                else:
                    self.add_item(self.items[item_name], quantity)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"{item_name} is not available.")

    # Method to remove item(s) from the cart
    def remove_item_from_cart(self):
        item_name = input("Enter the item name to remove from cart: ").strip().lower()
        self.remove_item(item_name)

    # Method to display details of the system management and allow user to interact with each choice.
    def start(self):
        while True:
            self.show_option()
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.view_items()
            elif choice == "2":
                self.add_items_to_cart()
            elif choice == "3":
                self.remove_item_from_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.print_receipt()
            elif choice == "6":
                print("Thank you for using the supermarket management system.")
                break
            else:
                print("Invalid option. Please try again.")


def main():
    system = GroceryManagement()
    system.start()


main()