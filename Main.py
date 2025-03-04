from Sales import Sales
from Product import Product

def display_menu():
    print("\n--- Cashier Management System ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display All Products")
    print("5. Display Stock")
    print("6. Make a Sale")
    print("7. View sales")
    print("8. Display total sales")
    print("9. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Product
            code = input("Enter product code: ")
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            qty = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            location = input("Enter product location: ")

            product = Product(code, name, description, qty, price, location)
            product.add_product()

        elif choice == "2":
            # Update Product
            update_cat = ""
            while True:
                product_code = input("Enter product code to update: ")
                
                print("\n--- Product Update Options ---")
                print("1. Update Quantity")
                print("2. Update Price")
                print("3. Update Location")

                update = input("Enter your choice: ")

                if update == "1":
                    new_quantity = int(input("Enter new quantity: "))
                    update_cat = "Quantity"
                    Product.update_product(product_code,update_cat,new_quantity)
                       
                elif update == "2":
                    new_price = float(input("Enter new price: "))
                    update_cat = "Price"
                    Product.update_product(product_code,update_cat,new_price)
                    
                elif update == "3":
                    new_location = input("Enter new location: ")
                    update_cat = "Location"
                    Product.update_product(product_code,update_cat,new_location)
                    
                else:
                    print("Invalid choice. Please select a valid option.")
                

        elif choice == "3":
            # Delete Product
            product_code = input("Enter product code to delete: ")

            product = Product(None, None, None, None, None, None)  # Create a dummy product to access methods
            product.delete_product(product_code)

        elif choice == "4":
            # Display All Products
            product = Product(None, None, None, None, None, None)  # Create a dummy product to access methods
            products = product.read_products()
            for p in products:
                p.display_data()
                print("-" * 30)

        elif choice == "5":
            # Make a Sale
            product_code = input("Enter product code: ")
            quantity_sold = int(input("Enter quantity sold: "))

            # Assuming Sales class has a method to handle sales
            sale = Sales()
            sale.make_sale(product_code, quantity_sold)

        elif choice == "6":
            # Exit
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()