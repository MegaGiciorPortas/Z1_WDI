tablica = []
n = -1
suma = 0
while n != 0:
    n = int(input("n: "))
    tablica.append(n)

for i in range(len(tablica)):
    if i == 0:
        if tablica[i] == sum(tablica[1:5]) / 4:
            print(tablica[i])
    elif i == 1:
        suma = tablica[i - 1] + sum(tablica[i + 1:i + 4])
        if tablica[i] == suma / 4:
            print(tablica[i])
    elif i == len(tablica) - 2:
        suma = sum(tablica[i - 3:i]) + tablica[i + 1]
        if tablica[i] == suma / 4:
            print(tablica[i])
    elif i == len(tablica) - 1:
        suma = sum(tablica[i - 4:i])
        if tablica[i] == suma / 4:
            print(tablica[i])
    else:
        suma = tablica[i - 2] + tablica[i - 1] + tablica[i + 2] + tablica[i + 1]
        if tablica[i] == suma / 4:
            print(tablica[i])
