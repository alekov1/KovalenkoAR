def Numbers(x, y):
    count_day = 1
    while x < y:
        x = x * 1.1
        count_day += 1
    return count_day

x = int(input())
y = int(input())

print(Numbers(x,y))
