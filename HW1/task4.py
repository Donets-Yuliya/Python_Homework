temperatures = [18, 19, 21, 20, 22, 28, 30, 27, 15, 16, 18, 17, 25, 24, 26, 10, 12, 11, 13, 12]

result_list = []

temp_list = []
sort_list = []

for temp in temperatures: 
    if not temp_list: 
        temp_list.append(temp)
        sort_list.append(temp)
    # проверяем разницу между минимальной/максимальной температурой из промежутка и текущей температурой
    elif abs(temp - sort_list[0]) <= 4 and abs(temp - sort_list[-1]) <= 4:
        temp_list.append(temp)
        sort_list.append(temp)
        sort_list.sort()
    # проверяем количество дней стабильной температуры
    elif len(temp_list) >= 3: 
        result_list += [temp_list]
        temp_list = [temp]
        sort_list = [temp]
    else: 
        temp_list = [temp]
        sort_list = [temp]

print(*result_list, sep=",\n")
