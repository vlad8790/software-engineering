import for_triangle

a = float(input("������� �������� ����� a: "))
b = float(input("������� �������� ����� b: "))
c = float(input("������� �������� ����� c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("������� ������� ������� ������������")
else:
    print(for_triangle.triangle(a,b,c))