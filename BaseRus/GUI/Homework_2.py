"""
1) Создайте окно с меткой, где должно выводиться случайное целое число от 1 до 1000.
Примечание: то есть при каждом запуске программы там должно появляться случайное число.
"""

from tkinter import *
from random import *

def setWindow(root):
    root.title("Окно программы")  # Задаем название окна
    root.resizable(False, False)  # Запрещаем изменение размеров окна по горизонтали и вертикали

    w = 800  # Задаем ширину окна
    h = 600  # Задаем высоту окна
    ws = root.winfo_screenwidth()  # определяем разрешение экрана по ширине
    wh = root.winfo_screenheight()  # определяем разрешение экрана по высоте

    x = int(ws / 2 - w / 2)  # Вычисляем x для вывода окна в средине экрана
    y = int(wh / 2 - h / 2)  # Вычисляем y для вывода окна в средине экрана

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Выводим окно в центре экрана

root = Tk()  # Создаем класс окна
setWindow(root)

str = randrange(1, 100, 1)

label = Label(root, text = str, font = "Tahoma 36", bg = "#ABFF99", fg ="Red")

label.pack()

root.mainloop()  # Цикл вызова окна