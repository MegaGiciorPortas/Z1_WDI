s = float(input("S: "))
a = 1
eps = 1e-6
diff = -a

while abs(diff) > eps:
    diff = -a
    a = (S / a + a) / 2
    diff += a

print()
