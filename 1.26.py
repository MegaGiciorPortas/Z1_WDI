import math

n = int(input("n: "))

a1 = 1
a2 = 1
tablica = []

while a1 <= n:
    tablica.append(a1)
    a1, a2 = a2, a1 + a2

flaga = False

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0 and i in tablica:
        if (n // i) in tablica:
            flaga = True
            break

if flaga:
    print("TAK")
else:
    print("NIE")

