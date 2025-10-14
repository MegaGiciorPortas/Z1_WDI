max_licznik = 0
a1 = 0
for i in range(2, 10000):
    licznik = 0
    an = i
    while an != 1:
        an = (an % 2) * (3 * an + 1) + (1 - an % 2) * an / 2
        licznik += 1

    if licznik == i:
        print(i)
        break