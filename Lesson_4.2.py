bas_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [bas_list[i] for en, i in enumerate(range(0, len(bas_list))) if bas_list[en] > bas_list[en - 1]]
print(b)
# Не понял как начать со второго элемента списка

# b = [bas_list[i] for i in range(1, len(bas_list)) if bas_list[i] > bas_list[i - 1]]