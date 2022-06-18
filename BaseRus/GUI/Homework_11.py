"""
1) Сделайте 4 элемента Label, задав у них одинаковые параметры width и height.
2) Выведите первый Label вверху по центру, второй и третий слева и справа соответственно под первым элементом,
   а четвёртый по центру снизу.
"""

from tkinter import *

def setwindow(root):
    root.title("Домашняя работа №11")
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

label1 = Label(root, text="Метка 1", font="Tahoma 20", width=18, height=2, bg="red")
label2 = Label(root, text="Метка 2", font="Tahoma 20", width=18, height=2, bg="green")
label3 = Label(root, text="Метка 3", font="Tahoma 20", width=18, height=2, bg="blue")
label4 = Label(root, text="Метка 4", font="Tahoma 20", width=18, height=2, bg="#9a3")

"""
label1.pack(side='top', fill=X, expand=True, anchor='n')
  side= - расположение по сторонам (top - сверху, left - слева, right - справа, bottom - снизу)
  fill= - растянуть объект по координате (X - по Х, Y - по Y)
  expand= - расширить метку по центру оставшейся области
  anchor= - якорь зацепляет по сторонам света (n - север, nw - северо-запад, ne - север-восток, s - юг , w - запад,
            e - восток, se - юго-восток, sw - юго-запад)
"""
label1.pack(side='top', anchor='n')
label2.pack(side='left', anchor='nw')
label3.pack(side='right', anchor='ne')
label4.pack(side='bottom')

root.mainloop()