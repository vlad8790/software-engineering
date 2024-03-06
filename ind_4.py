sen = input("Введите предложение: ")
print("Длина предложения -",len(sen))
print("В нижнем регистре: \n " + sen.lower())
vowels = 'aeiou'
count = 0
for i in range(5):
    count += sen.count(vowels[i])
print("Количество гласных 'a, e, i, o ,u' равно ",count)
print("'ugly' заменено на 'beauty': \n " + sen.replace('ugly','beauty'))
if sen.startswith("The"):
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")
if sen.endswith("end"):
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")