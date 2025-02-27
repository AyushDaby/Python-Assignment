#Creating Super class Sales:
class Sales:
    #Constructor Method
    def __init__(self, prod_code, prod_name, prod_price, prod_qty, total_cost, tax_rate, discount_rate):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.prod_price = prod_price
        self.prod_qty = prod_qty
        self.total_cost = total_cost
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate
        
    
    #Getters Methods
    def get_prod_code(self):
        return self.prod_code
    
    def get_prod_name(self):
        return self.prod_name 
    
    def get_prod_price(self):
        return self.prod_price
            
    def get_prod_qty(self):
        return self.prod_qty
            
    def get_total_cost(self):
        return self.total_cost
            
    def get_tax_rate(self):
        return self.tax_rate
            
    def get_discount_rate(self):
        return self.discount_rate
    
    
    #Setters Methods
    def set_prod_code(self, prod_code):
        self.prod_code = prod_code
    
    def set_prod_name(self, prod_name):
        self.prod_name = prod_name
        
    def set_prod_price (self, prod_price):
        self.prod_price = prod_price
        
    def set_prod_qty(self, prod_qty):
        self.prod_qty = prod_qty
        
    def set_total_cost(self, total_cost):
        self.total_cost = total_cost
        
    def set_tax_rate(self, tax_rate):
        self.tax_rate = tax_rate
        
    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate
        
        
    #Displaying values from methods
    def display_data(self):
        print(f"Product code: {self.prod_code}")
        print(f"Product name: {self.prod_name}")
        print(f"Quantity in stock: {self.prod_qty}")
        print(f"Product unit price: {self.prod_price}")
        print(f"Total cost: {self.total_cost}")
        print(f"Tax rate: {self.tax_rate}")
        print(f"Discount rate: {self.discount_rate}")
    