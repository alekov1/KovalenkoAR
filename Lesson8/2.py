def NumberSystem(X):
    return oct(X)[2:]

S = str(NumberSystem(2523))

if len(S) < 10:
    S = '0'*(10-len(S)) + S
print(S)

