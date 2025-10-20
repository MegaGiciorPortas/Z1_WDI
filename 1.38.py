def An(an_1, an_2, bn_1):
    return an_1 - bn_1 * an_2


def Bn(bn_1, an_1):
    return bn_1 + 2 * an_1


an_2 = 0
an_1 = 1
bn_1 = 2

licznik = 0
wynik = ""

while True:
    try:
        a = int(input(""))
    except ValueError:
        break

    if licznik == 0:
        if a == 0:
            wynik += str(bn_1) + ", "
            licznik += 1
        else:
            break
    elif licznik == 1:
        if a == 1:
            bn_1 = Bn(bn_1, 0)
            wynik += str(bn_1) + ", "
            licznik += 1
        else:
            break
    else:
        an = An(an_1, an_2, bn_1)
        if a == an:
            bn = Bn(bn_1, an_1)
            wynik += str(bn) + ", "
            an_2, an_1, bn_1 = an_1, an, bn
        else:
            break
print("\n")
print(wynik.rstrip(","))
