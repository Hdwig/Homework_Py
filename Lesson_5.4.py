def some_sti(slv, tire, num):
    if slv == "One":
        slv = "Один"
    if slv == "Two":
        slv = "Два"
    if slv == "Three":
        slv = "Три"
    if slv == "Four":
        slv = "Четыре"
    tire = " - "
    q = [slv + tire + num]
    return q


a = 1
r = []
with open('zadanie_4.txt', "r") as file:
    while True:
        content = file.readline()
        b = [i for i in content.split()]
        f = some_sti(b[0], b[1], b[2])
        r.append(f)
        if a == 4:
            break
        a += 1

with open('zadanie_41.txt', "w+") as new_file:
    for i in r:
        i += "\n"
        new_file.writelines(i)
