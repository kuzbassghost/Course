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

label = Label(root, text="Ваш любимый цвет", font="Tahoma 20")

choice1 = StringVar()
r1 = Radiobutton(root, text="Красный", font="Tahoma 20", variable=choice1, value="red")
r2 = Radiobutton(root, text="Зеленый", font="Tahoma 20", variable=choice1, value="green")
r3 = Radiobutton(root, text="Синий", font="Tahoma 20", variable=choice1, value="blue")

choice1.set("green")

print(choice1.get())

choice2 = IntVar()

r4 = Radiobutton(root, text="Красный", font="Tahoma 20", variable=choice2, value=1)
r5 = Radiobutton(root, text="Зеленый", font="Tahoma 20", variable=choice2, value=2)
r6 = Radiobutton(root, text="Синий", font="Tahoma 20", variable=choice2, value=3)

choice2.set(2)

label.pack()  # вызов паковщика - вывод кнопки 1
r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()

root.mainloop()  # Цикл вызова окна
