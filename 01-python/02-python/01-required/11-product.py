class Product:

    def __init__(self, price, name, weight, brand, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        x = str(tax)
        if (x[:2] != "0."):
            print("Tax multiplier must begin with '0.'\n")
            return -1
        else:
            print(f"Price with tax: {self.price * tax}")
            return self.price * tax

    def displayInfo(self):
        print(f"Price: {self.price}")
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight}")
        print(f"Brand: {self.brand}")
        print(f"Status: {self.status}\n")
        return self
    
    def reason_for_return(self, reason):
        reasons = ['defective', 'like_new', 'opened']
        if reason not in reasons:
            print("Please specify valid reason.\n")
        if (reason == 'defective'):
            self.status = reason
            self.price = 0
            return self
        elif (reason == 'like_new'):
            self.status = 'like new'
            self.price
            return self
        elif (reason == 'opened'):
            self.status = 'used'
            self.price *= .2
            return self

# test methods
bfg = Product(10000, 'BFG 9000', 15, 'iD')
bfg.displayInfo().add_tax(10)
bfg.sell().add_tax(0.02)
bfg.displayInfo()

lollipop = Product(1, 'Purple Pop', 1, 'Willy Wonka')
lollipop.reason_for_return('foo')
lollipop.reason_for_return('opened').displayInfo()
lollipop.reason_for_return('like_new').displayInfo()
lollipop.reason_for_return('defective').displayInfo()

# note that setting 'defective' above the others will keep price at 0, normally there'd be a price in the DB to reapply when changing to like_new or opened
