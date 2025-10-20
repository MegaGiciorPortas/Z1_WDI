a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))
wynik = ""
while e != 0:
    if c == (a + b + d + e) / 4:
        wynik += str(c) + ", "
    a = b
    b = c
    c = d
    d = e
    e = int(input("e: "))

print(wynik)