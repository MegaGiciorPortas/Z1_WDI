def func(n, p):
    suma = 0
    while n > 0:
        suma += (n % 10) ** p
        n = n // 10
    if suma == 216 and n == 0:
        return True
    return False

# p = int(input("p: "))
# x = int("9" * p)
#
# while x >= 600:
#     if func(x, p):
#         print(x)
#         break
#     x -= 1
#     if x < 10 ** (p - 1):
#         p -= 1

n = int(216 * "1")
print(func(n,216))