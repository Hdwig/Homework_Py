
with open('test_text_1.txt', "w") as file:
    while True:
        a = input("Введите любые данные, для окончания записи нажмите Enter в пустой строке: ")
        if a == "":
            break
        file.write(a + "\n")
