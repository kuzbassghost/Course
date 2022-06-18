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

def handlerenter(event):
    event.widget.config(bg="red")

def handlerleave(event):
    event.widget.config(bg="yellow")

root = Tk()
setwindow(root)

button1 = Button(root, text="Кнопка1", font="Tahoma 20", bg="yellow")
button2 = Button(root, text="Кнопка1", font="Tahoma 20", bg="yellow")

button1.bind("<Enter>", handlerenter)
button1.bind("<Leave>", handlerleave)
button2.bind("<Enter>", handlerenter)
button2.bind("<Leave>", handlerleave)

button1.pack()
button2.pack()

root.mainloop()