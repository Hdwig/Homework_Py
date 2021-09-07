result = {}
with open("list.txt") as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        hours = 0
        for elem in data[1:]:
            if elem != "-":
                num = "0"
                for z in elem:
                    if z.isdigit():
                        num += z
                    else:
                        break
                hours += int(num)
        result.update({data[0].strip(':'): hours})
print(result)
# Подсмотрел, но понял
