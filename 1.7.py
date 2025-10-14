s = float(input("S: "))
a = 0
b = 1
eps = 1e-6

while abs(b - a) > eps:
    a = b
    b = (s / b + b) / 2
print(b)
