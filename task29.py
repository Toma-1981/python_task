# Задача вместо 29:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random
numList = [str(random.randint(1000, 9999)) for i in range(7)]
print(numList)

numberToRemove = input('Введите цифру для удаления: ')
newList = []
for i in numList:
    i = i.replace(numberToRemove, "")
    newList.append(i)
print(newList)

def sumOfNum(num):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    if sum < 10:
        return sum
    num = str(sum)
    return sumOfNum(num)

myList = []
for num in newList:
    myList.append(sumOfNum(num))
print(myList)

setNum = set(myList)
print(setNum)

