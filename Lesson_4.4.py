from itertools import count
b = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
f = [i for i in b if b.count(i) == 1]
print(f)
