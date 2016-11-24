def square(val):
    return val * val


def getSumSquare():
    sumSquare = 0
    for i in range(1, 101, 1):
        sumSquare += square(i)

    return sumSquare


def getSquareSum():
    firstSum = 0
    squareSum = 0
    for i in range(1, 101, 1):
        firstSum += i

    squareSum = square(firstSum)
    return squareSum


print getSquareSum() - getSumSquare()
