"""
1) Добавьте scrollbar к текстовой области из упражнения к уроку «Текстовая область».
Примечание: при необходимости в текстовый файл надо добавить ещё текста, чтобы scrollbar стал активным.
"""

from tkinter import *


def setWindow(root):
    root.title("Домашнее задание №8")  # Задаем название окна
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

text = Text(root, bd=2, font="Tahoma 20", bg="White", fg="Green", width=40)
scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

text['yscrollcommand'] = scrollbar.set

try:
    handler = open('a.txt', 'r')
    text.insert(END, handler.read())
    handler.close()
except FileNotFoundError:
    print("Файла не сущеcтвует")

text.pack(side='left')  # вызов паковщика - вывод
scrollbar.pack(side='left', fill=Y)
root.mainloop()  # Цикл вызова окна
