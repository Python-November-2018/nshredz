import random

# randInt() returns a random integer between 0 to 100
#def randInt():
#    return (random.random()*100)

#x = int(randInt())
#print(x)

# randInt(max=50) returns a random integer between 0 to 50
#def randInt(max=50):
#    return (random.random()*max)
#x = int(randInt())
#print(x)

# randInt(min=50) returns a random integer between 50 to 100
#def randInt(min=50):
#    y = 0
#    while (y < min):
#        y = random.random()*100
#    return(y)    
#x = int(randInt())
#print(x)

#randInt(min=50, max=500) returns a random integer between 50 and 500
def randInt(min=50, max=500):
    y = 0
    while (y < min and y < max):
        y = random.random()*max
    return y
for z in range(20):
    x = int(randInt())
    print(x) # afer looping a few times all appear to be between 50 and 500
