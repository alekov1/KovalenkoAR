#задание 1
def numbers(A: int, B: int):
    if A <= B:
        return [int(i) for i in range(A, B+1)]

for x in numbers(7, 15):
    print(x)
