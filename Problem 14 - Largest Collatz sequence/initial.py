import time

start = time.time()


def collatz(n):
    if n == 1:
        return n
    elif n % 2 == 0:
        n /= 2
        return n
    else:
        n = (3 * n) + 1
        return n


num = 0
max_len = 0
max_len_num = 0
counter = 0
lengths = []

for i in range(1, 10):
    num = i
    lst = [num]
    while num != 1:
        num = collatz(num)
        lst.append(num)
        counter += 1

        if num < i:
            lst_len
            break

    lst_len = len(lst)
    lengths[i] = lst_len

    if lst_len > max_len:
        max_len = lst_len
        max_len_num = i

elapsed = (time.time() - start)
print max_len
print max_len_num
print elapsed
