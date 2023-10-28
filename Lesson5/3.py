N = int(input())
x = 2
x1 = 2
count = 1

while x <= N:
    x = x * x1
    count += 1
count -= 1
x = 2
print(x**count, count)