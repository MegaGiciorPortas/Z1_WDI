from math import sqrt


def sumowanie(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma


def rozklad(n):
    czynnik = 2
    czynniki = []
    while czynnik * czynnik <= n:
        if n % czynnik == 0:
            czynniki.append(czynnik)
            n = n // czynnik
        else:
            czynnik += 1
    if n > 1:
        czynniki.append(n)

    suma = 0
    for x in czynniki:
        suma += sumowanie(x)
    return suma


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


licznik = 0
for x in range(2, int(1e6)):
    if not czy_pierwsza(x):
        if sumowanie(x) == rozklad(x):
            print(x)
            licznik += 1
print(licznik)
