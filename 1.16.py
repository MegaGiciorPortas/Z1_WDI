def nwd(a, b):
    while b != 0:
        print(a, b)
        a, b = b, a % b
    return a


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(nwd(nwd(a, b), c))
