a = int(input())
b = int(input())
c = int(input())
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    p = (a + b + c)/2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('Площадь треугольника:', S)
else:
    print('Ошибка')
