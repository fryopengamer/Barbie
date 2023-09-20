sides = input("Введите длины сторон треугольника через пробел: ")
sides = sides.split()
sides = [int(x) for x in sides]
sides = sorted(sides, reverse = True)
smax = 0

for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c)/2
                s = (p*(p-a)*(p-b)*(p-c))**(0.5)
                if s > smax:
                    smax = s
print("Максимальная площадь треугольника: ", smax)
