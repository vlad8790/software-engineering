value = 128
while value > 0:
    if value == 128:
        value -= 64
    elif value / 2 > 1:
        value /= 2
    else:
        value -= 1
    print(value)