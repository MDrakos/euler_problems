def checkVal(val):
    checkValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for i in checkValues:
        if val % i != 0:
            return 0

    return val


smallestMultipleList = []
smallestMultipleVal = 0
for i in range(0, 500000000, 1):
    if checkVal(i) != 0:
        smallestMultipleList.append(checkVal(i))

for j in smallestMultipleList:
    smallestMultipleVal = j
    break

print smallestMultipleVal

