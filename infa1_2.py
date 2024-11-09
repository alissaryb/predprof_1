#инфа 1, задача 2
for x in range(2, 37):
    for y in range(8, 37):
        a = int("111", x)
        b = int("337", y)
        if (a == b):
            print("ans", x)
            break
