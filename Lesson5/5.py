def Numbers(x):
    x = 0
    y = 1
    count = 0
    while y != 0:
        y = int(input())
        count += 1
    return count - 1

print(Numbers(1))
