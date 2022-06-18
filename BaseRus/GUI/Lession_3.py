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

button1 = Button(root, text = "Моя кнопка 1", font = "Tahoma 18", bg = "#ABFF99", fg ="Red") # Создание кнопки 1
# параметр text = - вывод текста метки, font = - шрифт метки, bg = - цвет фона метки, fg = цвет текста метки
button2 = Button(root, text = "Моя кнопка 2", font = "Tahoma 22", bg = "White", fg ="Blue") # Создание кнопки 2

button1.pack() # вызов паковщика - вывод кнопки 1
button2.pack() # вызов паковщика - вывод кнопки 2

root.mainloop()  # Цикл вызова окна