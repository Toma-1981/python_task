# Задача №31. 
# Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
fib1 = int(input('Введите номер числа Фибоначи: '))
def fibonachi(fib1):
    if fib1 == 1:
        return 1
    elif fib1 == 0:
        return 0
    else:
        return fibonachi(fib1 - 1) + fibonachi(fib1 - 2)
print(fibonachi(fib1))    