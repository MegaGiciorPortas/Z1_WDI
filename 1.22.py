f1 = int(input("f1: "))
f2 = int(input("f2: "))

while f1 <= 1e6:
    f1, f2 = f2, f1 + f2

lim = round(f2 / f1, 3)
print(lim)
