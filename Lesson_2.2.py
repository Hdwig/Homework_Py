lst = [u for u in input('Введите значения через пробел ').split()]
a = 0
e = len(lst)
while a < e - 1:
    lst[a], lst[a + 1] = lst[a + 1], lst[a]
    a += 2
print(lst)
