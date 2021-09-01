from itertools import cycle, count


q = int(input("Введите число с которого начать: "))
c = int(input("Введите число, на котором надо закончить цикл: "))
a = [i for i in range(q, c + 1) if i <= c]
print(a)
# Реализовал 2 скрипта, какой из них верный?
test_gen = count(q)
for i in test_gen:
    if i > c:
        break
    print(i)



print("Списк чисел, который был выведен, будет использоваться для зацикливания")
cw = int(input("Введите, сколько повторений цикла надо сделать: "))
t = 0
a_gen = cycle(a)
for i in a_gen:
    if i == q:
        t += 1
        if t == cw + 1:
            break
    print(i)

