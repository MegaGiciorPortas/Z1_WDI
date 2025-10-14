n = int(input("n: "))

n = str(n)
last = n[-1]
n = n[:len(n) - 1]

if last in n:
    print("NIE")
else:
    print("TAK")
