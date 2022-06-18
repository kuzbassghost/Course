"""
1) В цикле попросите пользователя вводить названия городов, каждый раз добавляя их в список.
2) Когда пользователь введёт 0, то нужно выйти из цикла.
3) Используя созданный список, выведите его с помощью Listbox в окно программы.
"""

from tkinter import *


def setWindow(root):
    root.title("Домашнее задание №9")  # Задаем название окна
    root.resizable(False, False)  # Запрещаем изменение размеров окна по горизонтали и вертикали

    w = 800  # Задаем ширину окна
    h = 600  # Задаем высоту окна
    ws = root.winfo_screenwidth()  # определяем разрешение экрана по ширине
    wh = root.winfo_screenheight()  # определяем разрешение экрана по высоте

    x = int(ws / 2 - w / 2)  # Вычисляем x для вывода окна в средине экрана
    y = int(wh / 2 - h / 2)  # Вычисляем y для вывода окна в средине экрана

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Выводим окно в центре экрана


data = []

while True:
    str = input("Введите строку: ")
    if str == "0":
        break
    data.append(str)

root = Tk()  # Создаем класс окна

setWindow(root)

list = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)

for d in data:
    list.insert(END, d)

list.select_set(1, 1)
indexes = list.curselection()

list.pack()
root.mainloop()  # Цикл вызова окна
