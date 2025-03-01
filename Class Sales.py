#Creating Super class Sales:
class Sales:
    #Constructor Method
    def __init__(self, prod_code, prod_name, prod_price, prod_qty, tax_rate, discount_rate, total_cost):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.prod_price = prod_price
        self.prod_qty = prod_qty
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate
        self.total_cost = total_cost
        
    
    #Getters Methods
    def get_prod_code(self):
        return self.prod_code
    
    def get_prod_name(self):
        return self.prod_name 
    
    def get_prod_price(self):
        return self.prod_price
            
    def get_prod_qty(self):
        return self.prod_qty
         
    def get_tax_rate(self):
        return self.tax_rate
            
    def get_discount_rate(self):
        return self.discount_rate
    
    def get_total_cost(self):
        return self.total_cost
    
    
    #Setters Methods
    def set_prod_code(self, prod_code):
        self.prod_code = prod_code
    
    def set_prod_name(self, prod_name):
        self.prod_name = prod_name
        
    def set_prod_price (self, prod_price):
        self.prod_price = prod_price
        
    def set_prod_qty(self, prod_qty):
        self.prod_qty = prod_qty
          
    def set_tax_rate(self, tax_rate):
        self.tax_rate = tax_rate
        
    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate
        
    def set_total_cost(self, total_cost):
        self.total_cost = total_cost
        
        
        
    #Calculating Total cost
    def calculate_Total_cost(self):
       subtotal = self.prod_price * self.prod_qty
       discount_amount = subtotal * (self.discount_rate / 100)
       subtotal_with_discount = subtotal - discount_amount
       tax_amount = subtotal_with_discount * (self.tax_rate / 100)
       self.total_cost = subtotal_with_discount + tax_amount
       return self.total_cost
        
    #Displaying values from methods
    def display_data(self):
        print(f"Product code: {self.prod_code}")
        print(f"Product name: {self.prod_name}")
        print(f"Quantity in stock: {self.prod_qty}")
        print(f"Product unit price: {self.prod_price}")
        print(f"Tax rate: {self.tax_rate}")
        print(f"Discount rate: {self.discount_rate}")
        print(f"Total cost: {self.total_cost}")
    
    
    
def main():
      
      prod_code= input("Enter product code: ")
      prod_name= input("Enter product name: ")
      prod_qty= int(input("Enter quantity in stock: "))
      prod_price= float(input("Enter product unit: "))
      discount_rate= float(input("Enter discount: "))
      tax_rate= float(input("Enter tax rate: "))   
      
      sale1 = Sales(prod_code, prod_name, prod_price, prod_qty, discount_rate, tax_rate, 0) 
    
      print("Item details for sale 1: ")
      sale1.display_data()
      
      total = sale1.calculate_Total_cost()
      print(f"The total cost for sale 1: {total}")
    
main()
