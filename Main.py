from Product import Product
from Grocery import Cashier, ProductManager

# Function to display the main menu and get the user's choice
def display_menu():
    print("\n--- Cashier Management System ---")
    print("1. Sales transactions and recording")
    print("2. Product and stock management")
    print("3. Close")
    print("-" * 30)
    category = input("Enter the field of operation: ")
    print("-" * 30)
    return category  # Return the user's choice

# Function to display the sales management menu
def sales_management_menu():
    print("\n--- Supermarket Cashier System ---")
    print("1. Display Products")
    print("2. Add to Cart")
    print("3. Checkout")
    print("4. Exit")
    print("-" * 30)

# Function to display the product management menu
def product_management_menu():
    print("\n--- Supermarket Product System ---")
    print("1. Add product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display All Products")
    print("5. Display All Stock")
    print("6. Exit")
    print("-" * 30)

# Main function to run the cashier management system
def main():
    while True:
        category = display_menu()  # Get the user's choice for the main menu
        if category == "1":
            transaction = Cashier()  # Create a single instance of Cashier for the session
            while True:
                sales_management_menu()
                choice = input("Enter your choice: ")  # Get the user's choice for the sales management menu
                print("-" * 30)

                if choice == "1":  # Display all products
                    transaction.display_products()

                elif choice == "2":  # Add a product to the cart
                    while True:
                        product_code = input("Enter Product Code: ")
                        check_code = ProductManager(product_code, None, None, None)

                        if not check_code.check_product_code():
                            print(f"Error: Product code '{product_code}' does not exist in the system.")
                        else:
                            try:
                                quantity = int(input("Enter Quantity: "))  # Get the quantity from the user
                                if quantity <= 0:
                                    print("Quantity must be a positive integer.")
                                    continue
                                transaction.add_to_cart(product_code, quantity)  # Add the product to the cart
                                
                            except ValueError:  # Handle invalid quantity
                                print("Invalid quantity. Please enter a number.")
                                continue

                            continue_more = input("Do you want to add more (yes/no): ")
                            if continue_more.lower() == "no":
                                break

                elif choice == "3":  # Proceed to checkout
                    transaction.checkout()

                elif choice == "4":  # Exit to the main menu
                    print("Return to main menu.")
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif category == "2":  # If the user selects product management
            while True:
                product_management_menu()
                choice = input("Enter your choice: ")  # Get the user's choice for the product management menu
                print("-" * 30)

                if choice == "1":  # Add Product
                    code = input("Enter product code: ")
                    check_code = Product(code, None, None, None, None, None)  # Create a dummy product to check if the code exists

                    if check_code.check_product_code():  # Check if the product code already exists
                        print(f"Error: Product code '{code}' already exists in the system.")
                    else:
                        name = input("Enter product name: ")
                        description = input("Enter product description: ")
                        qty = int(input("Enter product quantity: "))
                        price = float(input("Enter product price: "))
                        location = input("Enter product location: ")

                        product = Product(code, name, description, qty, price, location)
                        product.add_product()  # Add the product to the system

                elif choice == "2":  # Update Product
                    while True:
                        product_code = input("Enter product code to update: ")
                        print("-" * 30)
                        print("\n--- Product Update Options ---")
                        print("1. Update Quantity")
                        print("2. Update Price")
                        print("3. Update Location")
                        print("-" * 30)

                        update = input("Enter your choice: ")
                        print("-" * 30)

                        if update == "1":  # Update quantity
                            new_quantity = int(input("Enter new quantity: "))
                            update_cat = "Quantity"
                            product = Product(product_code, None, None, new_quantity, None, None)
                            product.update_product(product_code, update_cat, new_quantity)

                        elif update == "2":  # Update price
                            new_price = float(input("Enter new price: "))
                            update_cat = "Price"
                            product = Product(product_code, None, None, None, new_price, None)
                            product.update_product(product_code, update_cat, new_price)

                        elif update == "3":  # Update location
                            new_location = input("Enter new location: ")
                            update_cat = "Location"
                            product = Product(product_code, None, None, None, None, new_location)
                            product.update_product(product_code, update_cat, new_location)

                        else:
                            print("Invalid choice. Please select a valid option.")

                        proceed = input("Do you want to update again? (yes/no): ")  # Ask if the user wants to update again
                        if proceed.lower() == "no":
                            break  # Break out of the update loop
                        print("-" * 30)

                elif choice == "3":  # Delete Product
                    product_code = input("Enter product code to delete: ")
                    check_code = Product(product_code, None, None, None, None, None)

                    if not check_code.check_product_code() :
                        print(f"Error: Product code '{product_code} does not exist in the system.")
                    else:
                        product = Product(None, None, None, None, None, None)  # Create a dummy product to access methods
                        product.delete_product(product_code)

                elif choice == "4":  # Display All Products
                    product = Product(None, None, None, None, None, None)  # Create a dummy product to access methods
                    products = product.read_products()
                    for p in products:
                        p.display_product()
                        print("-" * 30)

                elif choice == "5":  # Display Stock
                    stock = Product(None, None, None, None, None, None)  # Create a dummy product to access methods
                    stock_display = stock.read_stock()  # Read stock information
                    for s in stock_display:
                        s.display_stock()
                        print("-" * 30)

                elif choice == "6":  # Exit to main menu
                    print("Return to main menu.")
                    break  # Break out of the product management loop

                else:
                    print("Invalid choice. Please try again.")

        elif category == "3":
            print(f"Application closed! Goodbye!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
