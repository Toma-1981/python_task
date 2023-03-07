# Задача №33. 
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# способ 1
import random
numberOfRatings = int(input('Введите количество оценок: '))
random_assessments = [random.randint(1,5) for _ in range(numberOfRatings)]
print(random_assessments)
i = 0
while i < len(random_assessments):
    if random_assessments[i] == 4 or random_assessments[i] == 5:
        random_assessments[i] = 1
    i += 1
print(random_assessments) 

#способ 2
# from random import randint
# numbers = []
# for i in range(10):
#     numbers.append(randint(1,5))
# print(numbers)

# max_count = max(numbers)
# min_count = min(numbers)
# print(max_count)
# print(min_count)
# for i in range(len(numbers)):
#     if numbers[i] == max_count:
#         numbers[i] = min_count
# print(numbers) 

#способ 3
# import random
# def change_grade(grade_list):
#     return str(grade_list.replace(str(max(grade_list)), str(min(grade_list))))
# amount = int(input('Введите количество оценок: '))
# grade_list = [random.randint(1,5) for grade in range(amount)]
# print(grade_list)
# print(change_grade (grade_list))
