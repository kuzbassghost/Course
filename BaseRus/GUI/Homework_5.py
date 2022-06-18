"""
1) Создайте текстовый файл с произвольным текстом.
2) Выведите текстовую область в окно, где должен быть выведен весь текст из файла, созданном в предыдущем пункте.
Примечание: разумеется, надо воспользоваться функциями для работы с файлами.
"""

from tkinter import *

def setWindow(root):
    root.title("Окно программы")  # Задаем название окна
    root.resizable(False, False)  # Запрещаем изменение размеров окна по горизонтали и вертикали

    w = 800  # Задаем ширину окна
    h = 600  # Задаем высоту окна
    ws = root.winfo_screenwidth()  # определяем разрешение экрана по ширине
    wh = root.winfo_screenheight()  # определяем разрешение экрана по высоте

    x = int(ws / 2 - w / 2)  # Вычисляем x для вывода окна в средине экрана
    y = int(wh / 2 - h / 2)  # Вычисляем y для вывода окна в средине экрана

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # Выводим окно в центре экрана


root = Tk()  # Создаем класс окна
setWindow(root)

text = Text(root, bd=2, font="Tahoma 18", bg="White", fg="Black",  padx=10, pady=20)
# параметр font = - шрифт метки, bg = - цвет фона метки, fg = цвет текста метки

#text.insert(END, "Hello\nWord") # ввод в текстовое поле
#print(text.get("1.0", END)) # вывод содержимого текстового поля в консоль

try:
    handler = open('a.txt', 'r')
    text.insert(END, handler.read())
    handler.close()
except FileNotFoundError:
    print("Файла не сущеcтвует")

text.pack()

root.mainloop()  # Цикл вызова окна