"""
1) Создайте 3 элемента Frame.
2) В первый Frame добавьте label с текстом «Важная форма».
3) Во второй Frame добавьте 2 текстовых поля.
4) В третий Frame добавьте кнопку «Отправить форму».
5) Разместите все 3 элемента Frame в окне.
"""


from tkinter import *

def setwindow(root):
    root.title("Домашнее задание №10")
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

frame1 = Frame(root, bg="Red", bd=1)
frame2 = Frame(root, bg="Blue", bd=10)
frame3 = Frame(root, bg="Yellow", bd=10)


label1 = Label(frame1, text="Важная форма", font="Tahoma 20")
text1 = Text(frame2, bd=2, font="Tahoma 18", bg="Yellow", fg="Green", width=50, height=4, padx=10, pady=20)
text2 = Text(frame2, bd=2, font="Tahoma 18", bg="Yellow", fg="Green", width=50, height=4, padx=10, pady=20)
button = Button(root, text = "Отправить форму", font = "Tahoma 18", bg = "#ABFF99", fg ="Red")

frame1.pack()
frame2.pack()
frame3.pack()
label1.pack()
text1.pack()
text2.pack()
button.pack()

root.mainloop()