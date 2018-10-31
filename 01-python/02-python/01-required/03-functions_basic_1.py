# prediction: 5
# output: 5
def a():
    return 5
print(a())

# prediction: 10
# output: 10
def a():
    return 5
print(a()+a())

# prediction: 5
# output: 5
def a():
    return 5
    return 10
print(a())

# prediction: 5
# output: 5
def a():
    return 5
    print(10)
print(a())

# prediction: 5, None
# output: 5, None
def a():
    print(5)
x = a()
print(x)   

# prediction: ??? i expect an error about adding None (no return output, unsure how python handles this)
# output: TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
#def a(b,c):
#    print(b+c)
#print(a(1,2) + a(2,3))

# prediction: 25 (as string)
# output:
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#print(a(2,5).__class__)

# prediction: 100, 10
# output: 100, 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # prediction: 7 output: 7
print(a(5,3)) # prediction: 14 output: 14
print(a(2,3) + a(5,3)) # prediction: 21 output: 21

# prediction: 8
# output: 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# prediction: 500, 500, 300, 300
# output: 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# prediction: 500, 500, 300, 500
# output: 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# prediction: 500, 500, 300, 300
# output: 500, 500, 300, 300

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# prediction: 1, 3, 2
# output: 1, 3, 2

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# prediction: 1, 3, 5, 10
# output: 1, 3, 5, 10

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)