# Задача №51. 
# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, 
# если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# # Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects):
    result, result1 = [], []
    for i in objects:
        if characteristic(i) == 0:
            result.append(i)
        else:
            result1.append(i)            
    if result == objects or result1 == objects:
        return True    
    return False

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values): 
    print('same')
else:
    print('different')