"""
1) Узнайте, какое исключение появляется при делении числа на 0.
2) Попросите пользователя ввести 2 числа.
3) Выведите результат деления.
4) Перехватите исключение при делении на 0 и выведите пользователю в качестве результата слово «бесконечность».
"""

a = float(input("Введите первое число:  "))
b = float(input("Введите второе число:  "))

try:
    c = a / b
except ZeroDivisionError:
    print("Полученный результат: бесконечность")

else:
    print("Спасибо закорректный ввод")
    print("Полученный результат: ", c)
finally:
    exit(0)