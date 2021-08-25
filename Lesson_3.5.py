def sum_num(new):
    global result
    for i in new:
        result = result + i
    print(result)
    return result


result = 0
u = "2"
print("Если хотите закончить цикл введите '!' в люом месте через пробел")
while u != "!":
    num = input("Введите значения через пробел: ")
    spis = num.split()
    new_spis = []
    for u in spis:
        if u == "!":
            break
        f = int(u)
        new_spis.append(f)
    sum_num(new_spis)
