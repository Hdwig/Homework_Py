with open("sum_list.txt", 'w') as file_num:
    inp = input("Введите любые числа через пробел")
    file_num.write(inp)

u = 0
with open("sum_list.txt") as sum:
    content = sum.readline().split()
    for i in content:
        u += (int(i))
    print(u)






