def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print((a * b * c) / nwd(nwd(a, b), c))
