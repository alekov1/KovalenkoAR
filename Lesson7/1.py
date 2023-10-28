def NameUser(N):
    array = []
    for i in range(N):
        array.append(int(input()))
    return array

MinIndexUser = NameUser(5)
print(MinIndexUser.index(min(MinIndexUser)))