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

choice = IntVar()
check = Checkbutton(root, bd=20, text="Согласие на обработку", variable=choice, onvalue=1, offvalue=0)  # Создание чекбокса

#check.select() # установка чекселекта
#check.deselect() # снятие чекселекта
choice.set(1) # установка чекселекта

print(choice.get()) #вывод состояния чекселекта

check.pack()  # вызов паковщика - вывод кнопки 1

root.mainloop()  # Цикл вызова окна
