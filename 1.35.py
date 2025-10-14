n = int(input("n: "))

n = str(n)
length = len(n)
flaga = False
for i in n:
    if int(i) == length:
        flaga = True

if flaga:
    print("TAK")
else:
    print("NIE")
