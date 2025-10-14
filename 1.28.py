def czy_palindrom(n):
    n = str(n)
    return n == n[::-1]


n = int(input("n: "))
print(czy_palindrom(n))
print(czy_palindrom(bin(n)))

