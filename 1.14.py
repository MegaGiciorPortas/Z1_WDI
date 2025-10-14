import math


def czy_doskonala(n):
    suma = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            suma += i
            if i != n % i:
                suma += n // 1

    if suma == n:
        return True
    return False


for i in range(2, int(1e6)):
    if czy_doskonala(i):
        print(i)
