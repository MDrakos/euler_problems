import math


def number_divisors(n):
    nod = 0
    sqrt = int(math.sqrt(n))

    for i in range(sqrt):
        if n % (i+1) == 0:
            nod += 2

    if sqrt * sqrt == n:
        nod -= 1

    return nod

number = 0
current = 1

while number_divisors(number) < 500:
    number += current
    current += 1

print number

