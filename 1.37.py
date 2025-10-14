x = 1
eps = 0.0001
while abs(x ** x - 2020) >= eps:
    x = round((x + 2020 / x) / 2,4)
    

print(x)
