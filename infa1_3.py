#инфа 1, задача 3

def help(x):
    m = set()
    for i in range(1, x+1):
        if x % i == 0:
            m.add(i)
    return m

Max = 0
a = 0
for i in range(100, 1000):
    m = help(i)
    if len(m) > Max:
        Max = len(m)
        a = i

print(a)
print("Ans", len(help(a)))