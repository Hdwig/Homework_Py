def div_num(num_1, num_2):
    a = 0
    num_22 = int(num_2)
    if num_22 < 20000:
        print(num_1)
    a += num_22
    return a


d = 0
c = 0
print("Эти сотрудники получают меньше 20 т.р.")
with open('zadanie_3.txt') as file:
    while True:
        conten = file.readline()
        if conten == "":
            break
        b = [i for i in conten.split()]
        d += div_num(b[0], b[1])
        c += 1
print(f"Средняя величина доходов сотрудников составляет: {d / c}")

