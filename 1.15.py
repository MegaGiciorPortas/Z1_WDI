import math


def suma_dzielnikow(n):
    suma = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            suma += i
            if i != n // i:
                suma += n // i

    return suma


for a in range(1, int(1e6)):
    sumA = suma_dzielnikow(a)
    if 1e6 > sumA > a and suma_dzielnikow(sumA) == a:
        print(a, sumA)
