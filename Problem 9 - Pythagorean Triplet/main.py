def square(x):
    return x * x


def check_pythagorean(a, b, c):
    sum_square = square(a) + square(b)

    if sum_square == square(c):
        return True
    else:
        return False


def check_sum(a, b, c):
    sum_val = a + b + c

    if sum_val == 1000:
        return True
    else:
        return False


for i in range(500):
    for j in range(500):
        for k in range(500):
            if check_pythagorean(i, j, k):
                if check_sum(i, j, k):
                    print i * j * k
                    break



