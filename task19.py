# Задача №19. 
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  
# K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3]
# n = int(input("Введите количество чисел: "))
# k = int(input("Введите число на сколько нужно сдвинуть: "))
# my_list = [i for i in range(n)]
# print(my_list)
# my_list_one = my_list[:k]
# my_list_two = my_list[k:]
# my_list_end = my_list_two + my_list_one
# print(my_list_end)


from random import randint
numbers = [i for i in range(16)]
k = int(input('Ведите число К: '))
print(numbers)
result = numbers[len(numbers) - k:len(numbers)]
for i in range(len(numbers) - k):
    result.append(numbers[i])

print (result)    
