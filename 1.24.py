import math

a = int(input("a: "))
b = int(input("b: "))

for i in range(int(1e4)):
    a, b = math.sqrt(a * b), (a + b) / 2.0

print(round(a, 5))
print(round(b, 5))
