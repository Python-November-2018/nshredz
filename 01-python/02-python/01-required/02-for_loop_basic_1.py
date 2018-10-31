# 1. Basic - Print all the numbers/integers from 0 to 150.

for x in range(151):
    print(x)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
#for x in range(0,1000001,5): # on my laptop it stops around ~150k or so, likely due to lack of memory
    print(x)

# 3. Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for x in range(101):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif (x % 5 == 0):
        print("Coding")
    else:
        print(x)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(5000001):
    if (x % 2 != 0):
        sum += x
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
for x in range(2018,1,-4):
    print(x)

# 6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum, mult):
    print(x)