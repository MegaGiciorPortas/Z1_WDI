import math

def suma_dzielnikow(n):
    suma = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            suma += i
            suma += n // i

    return suma


for a in range(1, int(1e6)):
    sumA = suma_dzielnikow(a)
    if sumA > a and suma_dzielnikow(sumA) == a:
        print(a,sumA)
