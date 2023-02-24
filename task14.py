# Задача 14: 
# Требуется вывести все целые числа степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
number = int(input('Ведите число: '))
prod = 0
degree = 0
while prod * 2 < number:
    prod = 2 ** degree
    print(prod, end = ' ')
    degree += 1