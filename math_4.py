#Доказательство, что функция возрастающая
from math import sqrt

for x in range(2, 1000000):
    print(sqrt(x-2) + sqrt(x-1) + sqrt(x+7) + sqrt(x+34))

#Если очень хочется, то стройте производную, она будет возрастать