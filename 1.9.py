def func(a):
    return a ** a - 2024


l = 2
r = 5
eps = 1e-6
while abs(r - l) > eps:
    m = (l + r) / 2
    if func(m) * func(l) <= 0:
        r = m
    else:
        l = m
print((l + r) / 2)
