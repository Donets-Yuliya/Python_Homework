temperatures = [18, 19, 21, 20, 22, 28, 30, 27, 15, 16, 18, 17, 25, 24, 26, 10, 12, 11, 13, 12]

result_list = []
temp_list = []

for temp in temperatures: 
    if not temp_list: 
        temp_list.append(temp)
    elif len([x for x in temp_list if abs(x - temp) <= 4]) == len(temp_list): 
        temp_list.append(temp)
    # проверяем количество дней стабильной температуры
    elif len(temp_list) >= 3: 
        result_list += [temp_list]
        temp_list = [temp]
    else: 
        temp_list = [temp]

print(*result_list, sep=",\n")
