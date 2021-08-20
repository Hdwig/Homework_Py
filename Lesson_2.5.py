i = int(input("vvedite chislo: "))
my_list = [7, 5, 3, 3, 2]
my_list_1 = my_list.copy()
my_list_1.reverse()
n = 0
g = int(my_list_1[n])
while i > g:
    n += 1
    g = int(my_list_1[n])
    if i >= 8:
        my_list_1.append(i)
        break
my_list_1.insert(n, i)
my_list_1.reverse()
print(my_list_1)




