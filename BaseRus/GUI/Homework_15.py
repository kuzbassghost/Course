"""
1) Сделайте кнопку с текстом «Сгенерировать случайное число».
2) При клике по кнопке под ней должно появляться случайное целое число от 1 до 100.
Примечание: для вывода сгенерированного числа используйте Label.
"""
from random import *
from tkinter import *

def setwindow(root):
    root.title("Домашняя работа №15")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)


def handlerclick1():
    global label
    rendom = randrange(0, 100)
    label.config(text=rendom)

button1 = Button(root, text="Сгенерировать случайное число", font="Tahoma 20", command=handlerclick1)
label = Label(root, text="", font="Tahoma 20")

button1.pack()
label.pack()
root.mainloop()