value = 1
for i in range(7):
    print(i)
    if value != 6:
        value += 1
    elif value == 6:
        value *= 5
    else:
        break
print(value)