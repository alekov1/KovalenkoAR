n = 9
count = 0
sum_numbers = 0
while n != 0:
    n = int(input())
    sum_numbers += n
    count += 1
print(sum_numbers // (count - 1))