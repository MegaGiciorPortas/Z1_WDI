import math

x = int(input("x: "))
diff = math.radians(x)
x = ((x % 360) / 180) * math.pi

cos_value = 0
for n in range(11):
    cos_value += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)

print(round(cos_value, 4))
