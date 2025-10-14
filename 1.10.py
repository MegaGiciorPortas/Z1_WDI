n = int(input("n: "))

a = 1
b = 1
while a * b < n:
    a, b = b, a + b

if a * b == n:
    print(a, b)
else:
    print("Nie ma takich liczb! ")

