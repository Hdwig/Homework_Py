from functools import reduce


def mul_nums(a, b):
    return a * b


b = [i for i in range(100, 1001, 2)]
c = reduce(mul_nums, b)
print(c)
