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
label4 = Label(root, text="Метка 3", font="Tahoma 20", bg="#9a3")
label5 = Label(root, text="Метка 3", font="Tahoma 20", bg="#777")

"""
label1.pack(side='top', fill=X, expand=True, anchor='n')
  side= - расположение по сторонам (top - сверху, left - слева, right - справа, bottom - снизу)
  fill= - растянуть объект по координате (X - по Х, Y - по Y)
  expand= - расширить метку по центру оставшейся области
  anchor= - якорь зацепляет по сторонам света (n - север, nw - северо-запад, ne - север-восток, s - юг , w - запад,
            e - восток, se - юго-восток, sw - юго-запад)
"""

label1.pack(side='left', fill=X, expand=True, anchor='n')
label2.pack(side='top')
label3.pack(side='top')
label4.pack(side='bottom')
label5.pack(side='bottom')

root.mainloop()