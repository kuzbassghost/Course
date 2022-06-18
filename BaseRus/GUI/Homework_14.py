"""
1) Попросите пользователя ввести путь к картинке.
2) Следующим шагом попросите его указать, с каким масштабом выводить изображение.
3) Выведите его в окно программы с указанным пользователем масштабированием, используя Label.
Примечание: нужно учесть, что, если пользователь вводит значения меньше 1, значит, он хочет его сжать, и для этого
потребуется функция subsample, а также перевод, например, 0.2 в число 5 (1 / 0.2).
"""

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

path = input("Введите путь к файлу изображения: ")

mashtab = input("Введите масштаб изображения: ")

root = Tk()
setwindow(root)

photo = PhotoImage(file=path)
if mashtab < 1:
    mashtab = 1 / mashtab
    bgimage = photo.subsample(mashtab, mashtab)
else:
    bgimage = photo.zoom(mashtab, mashtab)

bg = Label(root, image=bgimage)
bg.place(x=0, y=0, relwidth=1)

root.mainloop()