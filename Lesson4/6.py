def Numbers(N):
    S = [int(x) for x in range(1, N+1)]
    factor_N = 1
    ListOfFactorN = []
    for y in range(len(S)):
            factor_N = factor_N * S[y]
    ListOfFactorN.append(factor_N)
    return ListOfFactorN


N = int(input())
print(Numbers(N))
