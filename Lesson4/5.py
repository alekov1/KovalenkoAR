def Numbers(N):
    ListOfNumbers = [int(x)**3 for x in range(1, N+1)]
    return sum(ListOfNumbers)

N = int(input())
print(Numbers(N))
