# numbers = [15, 7, 28, 10, 21]
numbers = [4, 6, 2, 11, 1, 11, 5]
# numbers = [1, 1, 1, 1, 1, 1]
# numbers = [-4, -6, -2, -11, -1, -11, -5]

numbers.sort()
max_num = numbers[-1]  # максимальный элемент
numbers2 = [num for num in numbers if num < max_num]  # все элементы последовательности, кроме максимального

if numbers2: 
    second_max_num = numbers2[-1]
    print("Второй по величине элемент: " + str(second_max_num))
else: 
    print("Отсутствует второй по величине элемент")
