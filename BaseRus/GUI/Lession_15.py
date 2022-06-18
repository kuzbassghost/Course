from tkinter import *

def setwindow(root):
    root.title("Окно программы")
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


def handlerclick1(args):
    print(args)

def handlerclick2():
    print("Нажата кнопка")

def handlerclick3(event):
    print("Кликнули правой кнопкой мыши по кнопке: ")
    print(event.widget.cget('text'))

def handlerroot(event):
    print(event)
    print("Сработало событие")


button1 = Button(root, text="Кнопка1", font="Tahoma 20", command=lambda: handlerclick1("Кнопка1"))
button2 = Button(root, text="Кнопка2", font="Tahoma 20", command=handlerclick2)
button3 = Button(root, text="Кнопка3", font="Tahoma 20")

handler = button2.bind("<Button-3>", handlerclick3)
button3.bind("<Button-3>", handlerclick3)

button2.unbind(handlerclick3, handler) # отвезать обработчки событий

root.bind("a", handlerroot)
root.bind("<Control-c>", handlerroot)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()