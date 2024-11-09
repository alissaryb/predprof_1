n = 23

#Шаг 2, чтоб все значения были чётны
for a1 in range(2, 100, 2):
    for d in range(2, 100, 2):
        s = (2 * a1 + (n - 1) * d) // 2 * n
        if s == 966:
            print(a1, d, s)
            print("Ans", a1 + d * 4)
        if s > 966:
            break
