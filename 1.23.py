import math

e = 0
for i in range(int(1e4)):
    e += 1 / math.factorial(i)

print(round(e, 5))
