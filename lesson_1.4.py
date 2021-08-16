i = int(input("Введите любое положительное число: "))
d = 0
f = 0
while i > f:
    c = i % 10
    i = i // 10
    if c > d:
        d = c
print(d)

