# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0   нужно  2
import random

coins = int(input('Введите количество монет: '))
side_eagle = 0
side_tails = 0
for i in range(coins):
    side = random.randint(0, 1)
    print(f'сторона монеты {i + 1} равна {side}')
    if side ==1:
        side_eagle += 1
    else:
        side_tails += 1
if side_eagle < side_tails:
    print(f'нужно перевернуть {side_eagle} орла')
else:
    print(f'нужно перевернуть {side_tails} решки')

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
# if x == 0:
#     count_zero += 1
# else:
#     count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)
    
                    



    

