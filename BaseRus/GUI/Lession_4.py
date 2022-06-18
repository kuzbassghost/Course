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

entry1 = Entry(root, font = "Tahoma 18", bg = "#ABFF99", fg ="Red", bd = 4) # Создание текстового поля 1
# параметр font = - шрифт метки, bg = - цвет фона метки, fg = цвет текста метки
entry2 = Entry(root, font = "Tahoma 22", bg = "White", fg ="Blue", bd = 4, show = "*") # Создание текстового поля 2

entry1.insert(END, "Hello")
entry1.insert(END, "ABC")

print(entry1.cget('font')) # Вывод значения параметра заданного текстового поля на экран. Вариант 1
print(entry1['font']) # Вывод значения параметра заданного текстового поля на экран. Вариант2

entry1.pack() # вызов паковщика - вывод кнопки 1
entry2.pack() # вызов паковщика - вывод кнопки 2

root.mainloop()  # Цикл вызова окна