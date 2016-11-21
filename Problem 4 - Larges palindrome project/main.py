def is_pal(c):
    return int(str(c)[::-1]) == c

maxpal = 0

for i in range(999, 99, -1):
    for k in range(i, 99, -1):
        value = i * k
        if is_pal(value) and value > maxpal:
            maxpal = value

print maxpal