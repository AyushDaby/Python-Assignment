stock_file = "Assignment/stock.txt"
product_file = "Assignment/products.txt"

# Creating Superclass Product
class Product:
    # Constructor Method
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    # Getters methods
    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    # Setters Methods
    def set_product_id(self, product_id):
        self._product_id = product_id

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_stock(self, stock):
        self._stock = stock

    # Creating an str method to display the details of a Product object
    def __str__(self):
        return f"{self._product_id}: {self._name} (Price: Rs{self._price:.2f}, Stock: {self._stock})"


# Creating Superclass StockManager
class StockManager:
    # Constructor Method
    def __init__(self):
        self._products = self.load_products()

    # Method to load products from files
    def load_products(self):
        products = []  # Use a list to store product_id and stock
        
        try:
            # Open stock.txt to read stock data
            with open(stock_file, 'r') as file:
                for line in file:
                    product_id, stock = line.strip().split(',')
                    products.append({'product_id': product_id, 'stock': int(stock)})
            
        
            product_data = [] #Use a list to store all product details 
            # Open product.txt to read product details
            with open(product_file, 'r') as file:
                   for line in file:
                      product_data.append(line.strip().split(','))
            # Update products list with name and price
            for product in products:
                for data in product_data:
                    if product['product_id'] == data[0]:  # Match product_id
                        product['name'] = data[1]  # Update name
                        product['price'] = float(data[4])  # Update price
                        break  # Exit the loop once the product is found

            # Create Product objects
            product_objects = []
            for product in products:
                product_objects.append(Product(
                    product_id=product['product_id'],
                    name=product['name'],
                    price=product['price'],
                    stock=product['stock']
                ))
            return product_objects

        except FileNotFoundError:
            print("Error: Stock or product file not found.")#If the stock file or product file is not found, returns an error
            return []
        except Exception as e:
            print(f"Error loading products: {e}")#If product details fails to display, returns an error
            return []

    # Method to get the list of product
    def get_products(self):
        return self._products

    # Method to display product
    def display_products(self):
        print("\nAvailable Products:")
        for product in self._products:
            print(product)


# Creating Subclass Cashier that inherits from Superclass(StockManager)
class Cashier(StockManager):
    # Constructor Method
    def __init__(self):
        super().__init__()
        self._cart = []

    # Method to add item(s) and quantity to cart
    def add_to_cart(self, product_id, quantity):
        for product in self._products:
            if product.get_product_id() == product_id: #if product_id is the same as it is in the product list 
                if product.get_stock() >= quantity:#if stock available for a product is less than quantity entered
                    product.set_stock(product.get_stock() - quantity)
                    self._cart.append({'product': product, 'quantity': quantity})
                    print(f"Added {quantity} units of {product.get_name()} to cart.")
                else:
                    print(f"Not enough stock for {product.get_name()}.")
                return
        print("Product not found.")

    # Method to checkout and display a receipt
    def checkout(self):
        if not self._cart:
            print("Your cart is empty. Add products before checking out.")
            return

        total = 0
        print("\n----------- Receipt -----------")#Printing a receipt after checkout 
        for item in self._cart:#Printing the details of items in the cart 
            product = item["product"]
            quantity = item["quantity"]
            cost = product.get_price() * quantity
            print(f"{product.get_name()} x {quantity}: Rs{cost:.2f}")
            total += cost
        print("-" * 30)
        print(f"Total: Rs{total:.2f}")
        print("-" * 30)
        print("Thank you for shopping with us!")
        print("-" * 30)
        self._cart.clear()


# Main Program
def main():
    cashier = Cashier()

    while True:
        print("\n--- Supermarket Cashier System ---")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        
        #Using a case statement to allow user to choose their operation.
        if choice == "1":
            cashier.display_products()#Display the product details available in the supermarket

        elif choice == "2":
            product_id = input("Enter Product ID: ").strip()#Enter the product ID 
            try:
                quantity = int(input("Enter Quantity: "))#Enter the Quantity for the product ID Above
                cashier.add_to_cart(product_id, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")#If either product ID or Quantity is invalid then display an error message

        elif choice == "3":
            cashier.checkout()#Display a receipt all items in the cart

        elif choice == "4":
            print("Exiting the system. Goodbye!")#If all is done with the above operations, it stops all operations and exit the system 
            break

        else:
            print("Invalid choice. Please try again.")



