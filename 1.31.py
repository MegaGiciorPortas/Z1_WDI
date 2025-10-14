n = int(input("Podaj ilosc prostokatow: "))
k = int(input("k: "))

dx = (k - 1) / n
x = 1

suma = 0
while x <= k:
    x = x + dx
    y = 1 / x
    suma += dx * y

print(suma)