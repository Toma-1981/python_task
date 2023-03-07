# Задача №39.
# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива 
# Ввод:                         Вывод:
# 7                             3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1               (каждое число вводится с новой строки)
import random
len_mass1 = int(input('Введите длину первого списка: '))
random_mass1 = [random.randint(1,30) for _ in range(len_mass1)]
len_mass2 = int(input('Введите длину второго списка: '))
random_mass2 = [random.randint(1,30) for _ in range(len_mass2)]
temp_list = []
print(random_mass1)
print(random_mass2)
for i in random_mass1:
    if i not in random_mass2:
        temp_list.append(i)
print(temp_list)        