for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            n1 = int(str(a) + str(b) + str(c))
            n2 = int(3 * str(b))

            if 3 * n1 == n2:
                print(f"a:{a},b:{b},c:{c}")