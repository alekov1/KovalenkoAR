def Numbers(a, b):
    if a <= b:
        return
    ListOfNumbers = []
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            ListOfNumbers.append(i)
    return ListOfNumbers

numbers = Numbers(13, 3)
print(numbers)
