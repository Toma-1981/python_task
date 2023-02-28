# Задача №21.
# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#          {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
import random
my_list = [random.randint(0,10) for _ in range(10)]
print(my_list) 
my_dict = {}
for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict) 

new_list = []
for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)

print(new_list)        