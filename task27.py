# Задача №27. 
# Пользователь вводит текст(строка). Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.
# Output: 19


string = input('Введите текст: ')
liststring = string.lower()
set = set(liststring.split())
print(len(set))


# другие способы
# string = 'Ручка тетрадь блокнот блокнот тетрадь'
# liststring = string.lower().split()
# print(string)
# print(liststring)
# catalog = {}
# for word in liststring:
#     catalog[word] = catalog.get(word, 0) + 1
# count = 0
# for _ in catalog:
#     count += 1
# print(count)

# key = catalog.keys()
# print(len(key))

# print(len(set(liststring)))


