class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, *args):
        for val in args:
            self.result += val
            #print(val)
        return self
    
    def subtract(self, *args):
        for val in args:
            self.result -= val
        return self

x = MathDojo()
print(x.add(2).add(2,5,1).subtract(3,2).result)
