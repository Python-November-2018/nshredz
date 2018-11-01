class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print(f"Price: {self.price}, top speed: {self.max_speed}, total miles: {self.miles}")
        return self # is there ever a reason to not return self? any point to to do in __init__ function?
    
    def ride(self):
        print("Riding.. vroom vroom vroom!")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing..")
        self.miles -= 5
        return self

fisher_price = Bike(5, 5)
fisher_price.ride().ride().ride().reverse().displayInfo()

radio_flyer = Bike(20, 60)
radio_flyer.ride().ride().reverse().reverse().displayInfo()

bfg900 = Bike(1000, 120)
bfg900.reverse().reverse().reverse().displayInfo()

# What would you do to prevent negative miles?
# add if statement to check for total miles before subtracting them and print message about how it cant go negative

# What methods can return self in order to allow chaining methods?
# I have returned self and chained ride() reverse() displayinfo() methods