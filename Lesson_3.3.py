def two_max_sum(num_1, num_2, num_3):
    min_two_max_sum = min(num_1, num_2, num_3)
    return num_1 + num_2 + num_3 - min_two_max_sum


n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n3 = int(input("Введите третье число: "))
print(two_max_sum(n1, n2, n3))

