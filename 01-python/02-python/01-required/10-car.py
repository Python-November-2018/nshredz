class Car:
    
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if (price < 10000):
            self.tax = 0.12
        else:
            self.tax = 0.15
        self.displayAll()

    def displayAll(self):
        print(f"Price: {self.price}")
        print(f"Speed: {self.speed}")
        print(f"Fuel: {self.fuel}")
        print(f"Mileage: {self.mileage}")
        print(f"Tax: {self.tax}\n")
        return self

slugbug = Car(2000, '35mph', 'Full', '15mpg')
prius = Car(2000, '5mph', 'Not Full', '105mpg')
pinto = Car(2000, '15mph', 'Kind of Full', '95mpg')
delorian = Car(2000, '25mph', 'Full', '25mpg')
studebaker = Car(2000, '45mph', 'Empty', '25mpg')
pt_cruiser = Car(2000000, '35mph', 'Empty', '15mpg')
