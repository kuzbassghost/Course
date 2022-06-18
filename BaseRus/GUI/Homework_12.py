"""
1) Используя place, создайте форму входа со следующими элементами: метку с текстом «Авторизация», под ней 2 текстовых
    поля и метки слева от них («Логин:», «Пароль:»), а уже под этими элементами выведите кнопку («Войти»).
    Примечание: разумеется, форма должна выглядеть аккуратно, всё должно быть выравнено.
"""

from tkinter import *

def setwindow(root):
    root.title("Домашнее задание №12")
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
botton = Button(root, text="Войти", font="Tahoma 20", width=180, height=20, fg="blue")

label1.place(relx=0.5, rely=0, anchor="n")
label2.place(x=15, y=40)
label3.place(x=15, y=80)
entry1.place(relx=0.25, rely=0.23)
entry2.place(relx=0.25, rely=0.43)
botton.place(relx=0.5, rely=0.65, width=200, height=50, anchor="n")

root.mainloop()