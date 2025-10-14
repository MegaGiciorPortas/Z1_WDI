from decimal import Decimal, getcontext

a = int(input("a: "))
b = int(input("b: "))
getcontext().prec = 100

wynik = Decimal(a) / Decimal(b)
print(f"{wynik}")
