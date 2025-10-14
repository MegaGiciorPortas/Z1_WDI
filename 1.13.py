import math as m

n = int(input("n: "))

i = 2
while i <= m.sqrt(n):
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1
if n > 1:
    print(n)
