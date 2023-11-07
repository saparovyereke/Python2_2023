class Product():
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        
    def get_price(self, kolichestvo):
        if kolichestvo == 10:
            return self.price*0.9
        elif 10<kolichestvo<99:
            return self.price*0.8
        else:
            return self.price
        
    def make_purchase(self, kol_pokupki):
        price = self.get_price(kol_pokupki)
        if kol_pokupki < self.amount:
            self.amount = self.amount - kol_pokupki
            print("Ok")
        else:
            print("Don't have enough")
            
            
    
        
    