def SumOfNumbers(N):
    ListOfNumbers = []
    for x in range(N):
        Numbers = int(input())
        ListOfNumbers.append(Numbers)
    return sum(ListOfNumbers)


N = int(input())
print(SumOfNumbers(N))
