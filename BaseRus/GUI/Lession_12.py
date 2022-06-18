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

label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="red")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="green")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="blue")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#9a3")
label5 = Label(root, text="Метка 5", font="Tahoma 20", bg="#777")

label1.place(x=5, y=10)  # вывести метку с заданными координатами
label2.place(relx=0.5, rely=0.5, anchor="center") # вывести метку посредине
label3.place(relx=0.5, rely=0, anchor="n") # вывести меткупосредине сверху
label4.place(relx=0.5, rely=0.7, width=70, height=100, anchor="center") # вывести метку определенных параметров
label5.place(relx=1, rely=0, anchor="ne") # вывести метку справа в верху

root.mainloop()