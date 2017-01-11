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

for i in range(1, 1000000):
    num = i
    lst = [num]
    while num != 1:
        num = collatz(num)
        lst.append(num)
        lst_len = len(lst)

        if lst_len > max_len:
            max_len = lst_len
            max_len_num = i

elapsed = (time.time() - start)
print max_len
print max_len_num
print elapsed


