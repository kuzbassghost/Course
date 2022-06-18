"""
1) Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
2) Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
3) Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных чисел.
Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.
"""

def isNum(d):
    numb = d%2
    if numb == 0:
        return True
    else:
        return False


def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

def bigsum(*numbers):
    s=0

    for n in numbers:
        s += n
    return s/len(numbers)

print(isNum(5))
print(getmax([1,5,9,7,14,35,2]))
print(bigsum(1,4,10,23,12,4))