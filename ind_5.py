import for_triangle

a = float(input("Введите значение длины a: "))
b = float(input("Введите значение длины b: "))
c = float(input("Введите значение длины c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Неверно указаны стороны треугольника")
else:
    print(for_triangle.triangle(a,b,c))