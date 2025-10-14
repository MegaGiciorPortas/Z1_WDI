n = int(input("n: "))
roznica = n

for i in range(int(n // 2), 0, -1):
    if n % i == 0:
        j = n // i
        if roznica > abs(i - j):
            roznica = abs(i - j)
            a, b = i, j

print(f"{n} = {a} * {b}")
