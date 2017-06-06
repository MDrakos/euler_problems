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
lengths = [0] * 1000000
lengths[1] = 1

for i in range(1, 1000000):
    num = i
    lst = [num]
    counter = 0
    while num != 1:
        num = collatz(num)
        lst.append(num)
        counter += 1

        # If length num is less then our current number then length has
        # already been calculated so we use our stored answer and add the counter
        if num < i:
            lengths[i] = lengths[num] + counter
            break

    lst_len = len(lst)
    lengths.append(lst_len)

for val in range(len(lengths)):
    if lengths[val] > max_len:
        max_len = lengths[val]
        max_len_num = val

elapsed = (time.time() - start)
print max_len
print max_len_num
print elapsed
