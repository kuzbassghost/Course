"""
1) Создайте свой модуль и подключите его в основном файле.
2) Напишите в модули 3 функции, каждая из которых принимает список. Первая функция – получение максимального значения,
    вторая – получение минимального значения, третья – получение суммы всех элементов.
3) Проверьте работу этих функций в основном файле.
"""

from Base import func

print("Используем наш модуль")


while True:
    print("1 - Получение максимального значения, 2 - Получение минимального значения, 3 - Получение суммы всех элементов, 0 - Выход")
    code = input("Введите команду:")
    if code =="0":
        exit()
    #a = float(input("Введите значения массива: "))
    if code == "1":
        r = func.max(1, 5, 9, 7, 14, 35, 2)
    elif code == "2":
        r = func.min(1, 5, 9, 7, 14, 35, 2)
    elif code == "3":
        r = func.sum(1, 5, 9, 7, 14, 35, 2)

    print("Результат: ", r)

