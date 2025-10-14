import math


def czy_pierwsza(n):
    if n == 2:
        return 1
    elif n < 2 or n % 2 == 0:
        return 0
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return 0
    return 1

n = int(input("n: "))
print(czy_pierwsza(n))