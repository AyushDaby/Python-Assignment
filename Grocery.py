# Creating superclass Grocery Item
class GroceryItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # Getter for name
    def get_name(self):
        return self._name
    
    # Getter for price
    def get_price(self):
        return self._price
    

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Setter for price
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Price must be a positive number.")

    def __str__(self):
        return f"{self._name}: Rs {self._price:.2f}"


# Creating second superclass shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart = []  

    # Method to add item
    def add_item(self, item, quantity):
        if quantity <= 0:
            print("Quantity must be a positive number.")
            return

        # Check if the item already exists in the cart
        for cart_item in self.cart:
            if cart_item["item"].get_name() == item.get_name():
                cart_item["quantity"] += quantity
                print(f"{quantity} {item.get_name()} added to cart.")
                return

        # If the item is not in the cart, add it
        self.cart.append({"item": item, "quantity": quantity})
        print(f"{quantity} {item.get_name()} added to cart.")

    # Method to remove item
    def remove_item(self, item_name):
        for cart_item in self.cart:
            if cart_item["item"].get_name().lower() == item_name.lower():
                self.cart.remove(cart_item)
                print(f"{item_name} removed from the cart.")
                return
        print(f"{item_name} is not in the cart.")

    # Method to view cart
    def view_cart(self):
        print("\nYour shopping cart:")
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = 0
            for cart_item in self.cart:
                item = cart_item["item"]
                quantity = cart_item["quantity"]
                item_total = item.get_price() * quantity
                total += item_total
                print(f"{item.get_name()}: Rs {item.get_price():.2f} X {quantity} = Rs {item_total:.2f}")
            print(f"Total: Rs {total:.2f}")

    # Method to print receipt
    def print_receipt(self):
        print("\n------ Receipt ------")
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = 0
            for cart_item in self.cart:
                item = cart_item["item"]
                quantity = cart_item["quantity"]
                item_total = item.get_price() * quantity
                total += item_total
                print(f"{item.get_name().capitalize()}: Rs {item.get_price():.2f} X {quantity} = Rs {item_total:.2f}")
            print("-" * 30)
            print(f"Total: Rs {total:.2f}")
            print("Thank you for shopping with us!")
        print("-" * 30)


# GroceryManagement class to inherit from ShoppingCart
class GroceryManagement(ShoppingCart):
    def __init__(self):
        super().__init__()  # Initialize the ShoppingCart
        self.items = {
            "apple": GroceryItem("Apple", 3.00),
            "milk": GroceryItem("Milk", 173.00)
        }

    # Method to show options
    def show_option(self):
        print("\nGrocery Management System:")
        print("1. View available items")
        print("2. Add items to cart")
        print("3. Remove item from the cart")
        print("4. View cart")
        print("5. Print receipt")
        print("6. Exit")

    # Method to view available items
   def view_items(self):
        print("\nAvailable Items:")
        for item_name, item in self.items.items():
            print(f"{item.get_name()}: Rs {item.get_price():.2f}")

    # Method to add items to cart
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

    # Method to remove items from cart
    def remove_item_from_cart(self):
        item_name = input("Enter the item name to remove from cart: ").strip().lower()
        self.remove_item(item_name)

    # Method to start the system
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


# Main function
def main():
    system = GroceryManagement()
    system.start()



main()
