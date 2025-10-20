n = int(input("n: "))
zera = 0
licznik = 1
while True:
    if 5 ** licznik > n:
        break
    zera += n // (5 ** licznik)
    licznik += 1

print(zera)