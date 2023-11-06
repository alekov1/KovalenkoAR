#Вариант 7
def CalculateAreaRightTriangle(X: float, Y: float):
    return 0.5 * X * Y
def CalculateAreaRectangle(X, Y, Z):
    p = (X + Y + Z) * 0.5
    return (p * (p - X) * (p - Y) * (p - Z)) ** 0.5

X = 8
Y = 9
Z = 10
T = 11

d = (X * X + Y * Y) ** 0.5

S = CalculateAreaRightTriangle(X, Y) + CalculateAreaRectangle(Z, T, d)

print(round(S))



