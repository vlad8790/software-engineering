from math import sqrt
def triangle(a,b,c):
    p = (a + b + c)/2
    result = sqrt(p*(p-a)*(p-b)*(p-c))
    return result
