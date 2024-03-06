val = int(input('Введите число от 0 до 10 включительно: '))
if val < 0 or val > 10:
    print("Число не в диапазоне от 0 до 10 включительно")
elif 0 <= val <= 3:
    print([0,1,2,3])
elif 3 < val < 6:
    print({3,4,5,6})
elif 6 <= val <= 10:
    print([6,7,8,9,10])
