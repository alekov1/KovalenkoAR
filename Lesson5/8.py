n = int(input())
k = []
k.append(n)
while n != 0:
    n = int(input())
    k.append(n)
count = 1
maxcount = 0
for x in range(1, len(k)):
    if k[x] == k[x-1]:
        count += 1
        maxcount = max(maxcount, count)
print(maxcount)
