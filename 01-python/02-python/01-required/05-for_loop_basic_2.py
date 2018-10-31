# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

#enumerate
def biggieSize(list):
    for (i, item) in enumerate(list):
        if (item > 0):
            list[i] = "big"
    return list

print(biggieSize([-1, 3, 5, -5]))


# for in range
def foo(arr):
    for i in range(len(arr)):
        if (i > 0):
            arr[i] = "big"
    return arr
print(biggieSize([-1, 3, 5, -5]))

#2. Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPos(list):
    count = 0
    for i in range(len(list)):
        if (i > 0):
            count += 1
            print(count)
        if (i == len(list)-1):
            list[i] = count
    return list

print(countPos([-1,1,1,1]))

#3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print (sumTotal([1,2,3,4]))

#4. Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def avgList(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return (sum / len(list))
print(avgList([1,2,3,4]))

#5. Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(list):
    count = 0
    for i in list:
        count += 1
    return count
print(length([1,2,3,4]))

#6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def min(list):
    min = list[0]
    for i in list:
        if (min > i):
            min = i
    return min
print(min([-1,-2,-3]))

#7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def max(list):
    max = list[0]
    for i in list:
        if (max < i):
            max = i
    return max
print(max([1,2,3,4]))

#8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def analyze(list):
    min = list[0]
    max = list[0]
    sumTotal = 0

    for i in list:
        if (max < i):
            max = i
        elif (min > i):
            min = i
        sumTotal += i
    newDict = {
        'max': max,
        'min': min,
        'sumTotal': sumTotal,
        'avg': sumTotal / len(list),
        'length': len(list)
    }
    return newDict
print(analyze([1,2,3,4]))

#9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverseList(list):
    temp = 0
    for i in (range(len(list) // 2)):
        temp = list[i]
        list[i] = list[len(list) - i - 1]
        list[len(list) - i - 1] = temp
    return list
print(reverseList([1,2,3,4]))