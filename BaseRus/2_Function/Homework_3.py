"""
1) Попросите пользователя указать, какое количество элементов надо создать в списке.
2) Сделайте цикл на соответствующее число итераций, в каждой из которых просите пользователя ввести число в таком
   формате: «Введите число N:», где N – текущий номер числа.
3) Добавляйте каждое это число в список.
4) По завершению цикла выведите получившийся список.
"""

number = int(input("Укажите количество элементов в списке: "))
list = []
n = 0
while n < number:
    num = int(input("Введите число N: "))
    list.insert(n, num)
    n += 1
print(list)