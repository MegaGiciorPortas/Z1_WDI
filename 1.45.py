from math import isqrt


def czy_palindrom(n):
    return n == n[::-1]


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for j in range(5, isqrt(n) + 1, 2):
        if n % j == 0:
            return False
    return True


def skracanie_liczby(napis):
    if len(napis) == 1:
        return ""
    if len(napis) == 3:
        return napis[1]
    return napis[1:len(napis) - 1]


n = int(input("n: "))
licznik = 0

if n >= 2:
    licznik += 1

for i in range(3, n, 2):
    if czy_pierwsza(i) and czy_palindrom(str(i)):
        flaga = True
        temp = skracanie_liczby(str(i))
        while temp != "":
            if czy_palindrom(temp) and czy_pierwsza(int(temp)):
                temp = skracanie_liczby(temp)
            else:
                temp = ""
                flaga = False
        if flaga:
            licznik += 1

print(licznik)
