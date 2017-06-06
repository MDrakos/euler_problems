def generateFib():
    fibList = [0,1]
    for i in range(2,100):
        fibList.append(fibList[i-1] + fibList[i-2])
    return fibList

def checkFib(arr):
    fibSum = 0

    for i in arr:
        if i < 4000000 and i % 2 == 0:
            fibSum += i
    print fibSum


myList = generateFib()
checkFib(myList)
