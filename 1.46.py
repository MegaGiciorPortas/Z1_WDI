from math import isqrt, sqrt

n = int(input("n: "))
m = int(input("m: "))

s = str(isqrt(m * 10 ** (2*n)))
suma = 0
for x in s[1:]:
    suma += int(x)
print(suma)


print(sqrt(2))
