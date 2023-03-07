# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random
len_list = int(input('Введите длину списка: '))
random_list = [random.randint(-10,10) for _ in range(len_list)]
print(random_list)
new_list = []
min_number = int(input('Введите минимум: '))
max_number = int(input('Введите максимум: '))
for i in range(len(random_list)):
    if min_number <= random_list[i] <= max_number:
        new_list.append(i)
print(new_list)