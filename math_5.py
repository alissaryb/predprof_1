v = []
for x in range(-10, 10):
    for y in range(-10, 10):
        if abs(y + 3) + abs(y - 2) <= 5 and x ** 2 + y ** 2 <= 8 and x * (y - x) >= 0:
            print("X", x, "Y", y)
            print(abs(y + 3) + abs(y - 2), "<=", 5)
            print(x ** 2 + y ** 2, "<=", 8)
            print(x * (y - x), ">=",  0)
            print()
            v.append((x, y))

ans = []
for i in v:
    ans.append(i[0] + i[1] * 3)

print(ans)
print("Ans", max(ans))

