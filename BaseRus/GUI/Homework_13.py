"""
1) Сделайте предыдущее упражнение, но уже используя grid.
"""

from tkinter import *

def setwindow(root):
    root.title("Домашнее задание №13")
    root.resizable(False, False)

    w = 400
    h = 200
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

label1 = Label(root, text="Авторизация", font="Tahoma 20", fg="red")
label2 = Label(root, text="Логин", font="Tahoma 14", fg="black")
label3 = Label(root, text="Пароль", font="Tahoma 14", fg="black")
entry1 = Entry(root, font="Tahoma 14", width=27, bg="#ABFF99", fg="blue", bd=1)
entry2 = Entry(root, font="Tahoma 14", width=27, bg="#ABFF99", fg="blue", bd=1, show="*")
button = Button(root, text="Войти", font="Tahoma 20", fg="blue")

#label1.grid(row=0, column=0, padx=10, pady=20)
label1.grid(row=0, column=0, columnspan=2,)
label2.grid(row=1, column=0, padx=20, pady=10)
label3.grid(row=2, column=0)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=0, columnspan=2, padx=40, pady=10, ipadx=100)

root.mainloop()