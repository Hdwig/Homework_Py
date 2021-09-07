import json

profit = {}
top_sps = []
average_tup = {}
average = 0
temp = 0
all = 0
o = 0
with open("text_file5_7.txt") as file:
    while True:
        first_sps = file.readline().split()
        pri = 0
        o += 1
        if int(first_sps[2]) > int(first_sps[3]):
            pri = int(first_sps[2]) - int(first_sps[3])
            temp += 1
        else:
            ubt = int(first_sps[2]) - int(first_sps[3])
        all += pri
        profit.update({first_sps[0]: pri or ubt})
        if o == 6:
            break

average = all / temp
average_tup.update({"average_profit": average})
top_sps.append(profit)
top_sps.append(average_tup)
print(top_sps)

with open("my_file.json", "w") as write_f:
    json.dump(top_sps, write_f)
