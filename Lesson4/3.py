def numbers(A: int, B: int):
    ListOfNumbers = []
    if A > B:
        while A != B-1:
            x = A
            if x % 2 != 0:
                ListOfNumbers.append(A)
                A -= 1
            else:
                A -= 1
    return ListOfNumbers
print(numbers(15, 1))
