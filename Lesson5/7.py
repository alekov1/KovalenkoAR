def numbers(x):
    x = 1
    n = -999999999999999
    count = 0
    while n != 0:
        n_last = n
        n = int(input())
        if n > n_last:
            count += 1
    return count - 1
print(numbers(1))
