n = int(input("n: "))

n = str(n)
q = int(n[1]) / int(n[0])
geometric = True
for i in range(1, len(n) - 1):
    if not int(n[i + 1]) / int(n[i]) == q:
        geometric = False

if geometric:
    print("Tak")
else:
    print("Nie")
