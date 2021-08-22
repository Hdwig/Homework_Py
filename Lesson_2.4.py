lst = [u for u in input('Введите значения через пробел ').split()]
for num, elem in enumerate(lst, 1):
    print(f"№{num}: {elem[:10]}")



