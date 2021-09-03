a = 1
with open('test_text.txt') as file:
    while True:
        content = file.readline()
        b = [i for i in content.split()]
        if content == "":
            break
        print(f"Строка: {a}, в ней  {len(b)} слов")
        a += 1






# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
