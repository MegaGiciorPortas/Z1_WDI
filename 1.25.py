import math


def czy_pierwsza(n):
    if n < 2:
        return False
    b = 2
    while b <= math.sqrt(n):
        if n % b == 0:
            return False
        b += 1
    return True

def czy_palindrom(s):
    s = str(s)
    if s == s[::-1]:
        return True
    return False

def usuwanie_cyfr(n):
    if n // 100 == 0:
        if czy_palindrom(n):
            return -1
        return -2
    s = str(n)
    return int(s[1:len(s) - 1])

n = int(input("n: "))
for i in range(1, n):
    a = i
    while czy_pierwsza(a) and czy_palindrom(a):
        a = usuwanie_cyfr(a)
        if a == -1:
            print(i)
