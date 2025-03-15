stock_file = "Assignment/stock.txt"
product_file = "Assignment/products.txt"

# Creating Superclass Product
class ProductManager:
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
    
    #Method to check product code
    def check_product_code(self):
        try:
            with open(product_file, "r") as checkfile: # Open product.txt to read product details
                for line in checkfile:
                    existing_product_id = line.strip().split(',')[0]
                    if existing_product_id == self._product_id:# If Product code exist in the file returns true
                        return True
            return False
        except FileNotFoundError:
            print("Error: Products file not found.")
            return False
        except Exception as e:
            print(f"An error occurred while checking the product code: {e}")
            return False


# Creating Superclass StockManager
class StockManager:
    # Constructor Method
    def __init__(self):
        self._products = self.load_products() # load products from files

    # Method to load products from files
    def load_products(self):
        products = []  # Use a list to store product_id and stock
        
        try:
            # Open stock.txt to read stock data
            with open(stock_file, "r") as file:
                for line in file:
                    product_id, stock = line.strip().split(',') # Split each line into product_id and stock
                    products.append({"product_id": product_id, "stock": int(stock)})
            
        
            product_data = [] #Use a list to store all product details 
            # Open product.txt to read product details
            with open(product_file, "r") as file:
                   for line in file:
                      product_data.append(line.strip().split(','))
            # Update products list with name and price
            for product in products:
                for data in product_data:
                    if product["product_id"] == data[0]:  # Match product_id
                        product["name"] = data[1]  # Update name
                        product["price"] = float(data[4])  # Update price
                        break  # Exit the loop once the product is found

            # Create Product objects
            product_objects = []
            for product in products:
                product_objects.append(ProductManager(product_id=product["product_id"], name=product["name"], price=product["price"], stock=product["stock"]))
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
        try:
            quantity = int(quantity)  # Ensure quantity is an integer
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                return
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            return

        product_found = False  # Using a Flag to check if the product is found
        for product in self._products:
            if product.get_product_id() == product_id:  # Check if product_id matches
                product_found = True  # Set the flag to True since the product is found
                if product.get_stock() >= quantity:  # Check if enough stock is available
                    # Check if the product is already in the cart
                    cart_item_found = False
                    for item in self._cart:
                        if item["product"].get_product_id() == product_id:
                            # Update the quantity if the product is already in the cart
                            item["quantity"] += quantity
                            cart_item_found = True
                            break

                    if not cart_item_found:
                        # Add the product to the cart if it's not already there
                        self._cart.append({"product": product, "quantity": quantity})

                    product.set_stock(product.get_stock() - quantity)  # Reduce stock by the quantity
                    print(f"Added {quantity} units of {product.get_name()} to cart.")
                else:
                    print(f"Not enough stock for {product.get_name()}.")
                break  # Exit the loop once the product is found and processed
        if not product_found:  # If the product was not found in the loop
            print("Product not found.")
            
            
    # Method to remove a product completely from the cart
    def remove_from_cart(self, product_id):
        for item in self._cart:
            if item["product"].get_product_id() == product_id:  # Check if product_id matches
                # Restore the stock
                item["product"].set_stock(item["product"].get_stock() + item["quantity"])
                # Remove the product from the cart
                self._cart.remove(item)
                print(f"{item['product'].get_name()} has been completely removed from the cart.")
                return
        print(f"Product with code '{product_id}' not found in the cart.")
        

    # Method to checkout and display a receipt
    def checkout(self):
        if not self._cart:  # Check if the cart is empty
            print("Your cart is empty. Add products before checking out.")
            return

        total = 0
        print("\n----------- Receipt -----------")  # Print receipt header
        for item in self._cart:  # Iterate through items in the cart
            product = item["product"]
            quantity = item["quantity"]
            cost = product.get_price() * quantity  # Calculate cost for the item
            print(f"{product.get_name()} x {quantity}: Rs{cost:.2f}")  # Print item details
            total += cost  # Add to total cost
        print("-" * 30)
        print(f"Total: Rs{total:.2f}")  # Print total cost
        print("-" * 30)
        print("Thank you for shopping with us!")  # Print thank you message
        print("-" * 30)
   
        self._cart.clear()  # Clear the cart after checkout
