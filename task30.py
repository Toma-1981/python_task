# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5 Вывод: 7 9 11 13 15
a1 = int(input('Введите начало: '))
d = int(input('Введите шаг: '))
n = int(input('Введите длину: '))
list = []
for i in range(n):
    list.append(a1 + i * d)

print(list)