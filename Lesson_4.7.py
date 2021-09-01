from math import factorial


def fact(u):
    for i in u:
        e = factorial(i)
        yield e


f = int(input("Введите число, до которого будут выдаваться факториалы чисел: "))
n = [i for i in range(1, f + 1)]

for el in fact(n):
    print(el, end = ' ')
