n = int(input("n: "))

n = str(n)
increase = True
for i in range(len(n) - 1):
    if not n[i] < n[i + 1]:
        increase = False

if increase:
    print("Tak")
else:
    print("Nie")
