# Задача №17. 
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
n = int(input("Введите количество чисел: "))
k = int(input("Введите число на сколько нужно сдвинуть: "))
my_list = [i for i in range(n)]
print(my_list)
my_list_one = my_list[:k]
my_list_two = my_list[k:]
my_list_end = my_list_two + my_list_one
print(my_list_end)