bas_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [bas_list[i] for i in range(1, len(bas_list)) if bas_list[i] > bas_list[i - 1]]
print(b)
# Изначально я пытался написать вот так вот, но естественно у меня ничего не вышло. Пытался понять как внутри
# генератора использовать перечесление. В итоге подстмотрел в следующем уроке.
# b = [i for num,i in enumerate(bas_list: 1) if i[num] > i[num + 1]]
