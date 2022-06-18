"""
1) Создайте список из 3-х элементов, где значениями будут 3 различных цвета.
2) При наведении курсора мыши на окно программы (именно на окно) цвет его фона должен меняться на случайный элемент из
списка, созданного в предыдущем пункте.
3) При уводе курсора мыши с окна программы цвет его фона должен возвращаться на цвет по умолчанию.
"""
from random import *
from tkinter import *


def setwindow(root):
    root.title("Домашняя работа №16")
    root.resizable(False, False)
    root.configure(bg="white")

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


def handlerenter(event):
    color = randrange(0, len(data))
    event.widget.config(bg=data[color])


def handlerleave(event):
    event.widget.config(bg="white")


data = ["red", "yellow", "green"]

root = Tk()
setwindow(root)

list = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)
for d in data:
    list.insert(END, d)

list.select_set(1, 1)
indexes = list.curselection()

root.bind("<Enter>", handlerenter)
root.bind("<Leave>", handlerleave)

list.pack()

root.mainloop()
