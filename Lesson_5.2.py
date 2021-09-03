a = 1
with open('zadanie_2.txt') as file:
    while True:
        content = file.readline()
        b = [i for i in content.split()]
        if content == "":
            break
        print(f"Строка: {a}, в ней  {len(b)} слов")
        a += 1

