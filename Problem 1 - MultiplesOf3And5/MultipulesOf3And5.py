def makeArray(size):
    arr = []

    for num in range(0,size):
        arr.append(num)

    return arr

def multiples(arr):
    sumVal = 0

    for val in arr:
        if val%3 == 0 or val%5 == 0:
            sumVal += val
            print val

    print sumVal

array = makeArray(1000)
multiples(array)