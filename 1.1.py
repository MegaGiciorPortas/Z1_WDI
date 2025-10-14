n = int(input("n: "))
for c in range(n - 1, 4, -1):
    for a in range(1, c):
        for b in range(1, c):
            if a * a + b * b == c * c:
                print(a, b, c)
