# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#    5   // 1 2 3 4 5  //  6 // -> 5
import random
len_mass = int (input('Введите длину массива: '))
number = int(input('Введите число для поиска: '))
random_mass = [random.randint(1,10) for _ in range(len_mass)]
min_delta = max(random_mass)
for i in range(len_mass):
    if abs(number - random_mass[i]) < min_delta:
        min_delta = abs(number - random_mass[i])
        search_number = random_mass[i]

print(f'массив: {random_mass}')
print(f'самый близкий элемент к заданному числу: {search_number}')
