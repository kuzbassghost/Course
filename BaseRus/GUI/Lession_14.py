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

photo = PhotoImage(file="test.png")
bgimage = photo.zoom(2, 3)

bg = Label(root, image=bgimage)

buttonimage = photo.subsample(4, 4)
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1)

button.pack()


root.mainloop()