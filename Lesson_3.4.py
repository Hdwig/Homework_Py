def my_func(x, y):
    print(x ** y)
    xw = 1
    while y < 0:
        xw *= x
        y += 1
    x = 1 / xw
    print(x)


num_1 = float(input("Введите число, которое нужно возвести в степень: "))
num_2 = int(input("Введите степень: "))
my_func(num_1, num_2)

