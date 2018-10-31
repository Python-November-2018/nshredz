# sort default is low to high, but can be sorted in reserve, i'm sure there's a more efficent way to do this
def selectSort(arr, sort=1):
    min = 0
    n = len(arr)
    t = min

    if (sort == 1):
        for i in range(len(arr)):
            t = min
            while (t < n):
                if (arr[t] < arr[min]):
                    arr[min], arr[t] = arr[t], arr[min]
                t += 1
            min += 1
    else:
        for i in range(len(arr)):
            t = min
            while (t < n):
                if (arr[t] > arr[min]): #reverse order
                    arr[min], arr[t] = arr[t], arr[min]
                t += 1
            min += 1
    return(arr)