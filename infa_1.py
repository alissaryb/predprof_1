from math import factorial

n = 12
k = 5

a = factorial(n) // (factorial(k) * factorial(n - k))
print(a)
n -= k
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)

print("Ans", a * b)
