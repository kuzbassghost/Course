""""
1) Выведите чекбокс, который при каждом запуске программы случайным образом должен быть либо включенным, либо выключенным.
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

frame1 = Frame (root, bg="Red", bd=1)
frame2 = Frame (root, bg="Blue", bd=10)

label1 = Label(frame1, text="Метка1", font="Tahoma 20")
label2 = Label(frame2, text="Метка2", font="Tahoma 20")
label3 = Label(frame2, text="Метка3", font="Tahoma 20")

frame1.pack()
frame2.pack()
label1.pack()
label2.pack()
label3.pack()

root.mainloop()  # Цикл вызова окна
