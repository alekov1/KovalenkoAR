# вариант 2
def numbersort(number: list, positive: bool):
    array = []
    for i in range(len(number)):
        if number[i] >= 0 and positive:
            array.append(number[i])
        elif number[i] < 0 and not positive:
            array.append(number[i])
    return array


spisok = [-7, 6, 8, -1, 11, -3, 0, 15, 8]
spisok_true = numbersort(spisok, True)
spisok_false = numbersort(spisok, False)
print(f"{spisok_true}\n{spisok_false}")