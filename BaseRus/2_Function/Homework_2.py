"""
1) Попросите пользователя ввести произвольную строку.
2) Выведите коды всех символов строки, введённой пользователем.
3) Попросите пользователя ввести строку, состоящую только из цифр.
4) Используя соответствующую функцию, проверьте введённую пользователем строку, и если он ввёл правильно,
   то написать «Спасибо!», иначе выбросить исключение, в обработке которого вывести строку «Некорректный ввод!».

"""

str1 = input("Введите произвольную строку:  ")
print(ord(str1))