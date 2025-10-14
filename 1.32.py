n = int(input("n: "))

found = False
a = 2
while True:
    if a > n:
        break
    if n % a == 0:
        found = True
        break
    a = 3 * a + 1

if found:
    print("TAK")
else:
    print("NIE")
