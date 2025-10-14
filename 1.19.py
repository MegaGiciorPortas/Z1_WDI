import math
a = math.sqrt(0.5)
p = a
for i in range(int(10e4)):
    a = math.sqrt(1*a)
    p *= a

pi = 2 / p
print(pi)
