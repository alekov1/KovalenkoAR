N = int(input())
if N < 2:
    print('error')
N1 = [int(x) for x in range(2, N+1) if N % x == 0]
print(min(N1))