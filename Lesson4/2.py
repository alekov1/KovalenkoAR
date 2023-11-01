def SquenceOfNumbers(A: int, B: int):
    if A < B:
        return [*range(A, B+1)]
    else:
        return [*range(A, B-1, -1)]
print(SquenceOfNumbers(15, 1))
