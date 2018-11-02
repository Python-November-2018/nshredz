class Animal:
    
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        print(f"{self.name} walks about a few paces.")
        self.health -= 1
        return self

    def run(self):
        print(f"{self.name} sprints for several paces!")
        self.health -= 5
        return self

    def display_health(self):
        print(f"{self.name} has total health of {self.health}.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170
    
    def fly(self):
        print(f"{self.name} flies around a bit, whipping its tail.")
        self.health -= 10
        return self

    def display_health(self):
        super().display_health()
        print(f"I am a dragon!")
        return self

bob = Animal("Bob")
bob.walk().walk().walk().run().run().display_health()

fido = Dog("Fido")
fido.walk().walk().walk().run().run().pet().display_health()

smaug = Dragon("Smaug")
smaug.fly().display_health()

# Below won't work, has no member in class
#bob.fly()
#bob.pet()
#smaug.pet()