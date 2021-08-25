def div_num(num_1, num_2):
    return num_1 / num_2


num_1 = float(input("Ведите первое число: "))
num_2 = float(input("Ведите второе число: "))
while num_2 == 0:
    num_2 = float(input("Введите другое Второе число: "))
    continue
print(div_num(num_1, num_2))


