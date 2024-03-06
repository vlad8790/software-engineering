value = 64
for i in range(2,6,2):
    for j in range(2,6,2):
        if i == j:
            value **= 1/j
        else:
            value /= j
        print(value)
print(value)