def afwfwaf(N):
    if N < 2:
        print('error')
    N1 = [int(x) for x in range(2, N + 1) if N % x == 0]
    return min(N1)

N = int(input())
print(afwfwaf(N))
