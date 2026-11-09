# numbers = [15, 7, 28, 10, 21]
numbers = [4, 6, 2, 11, 1, 11, 5]
# numbers = [1, 1, 1, 1, 1, 1]
# numbers = [-4, -6, -2, -11, -1, -11, -5]

max_num = max(numbers)  # максимальный элемент
numbers2 = [num for num in numbers if num != max_num]  # все элементы последовательности, кроме максимального

if numbers2: 
    second_max_num = max(numbers2)
    print(f"Второй по величине элемент: {second_max_num}")

else: 
    print("Отсутствует второй по величине элемент")
