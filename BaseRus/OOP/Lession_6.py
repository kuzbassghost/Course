class Shape:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print('(', self.x, ';', self.y, ')', sep='')

    def draw(self):
        print("Рисуем фигуру")




class Circle(Shape):
    r = 0

    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r

    def draw(self):
        print("Рисуем окружность (", self.x, ";", self.y, ";", self.r, ')', sep='')


class Rectangle(Shape):
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h

    def draw(self):
        print("Рисуем прямоугольник (", self.x, ";", self.y, ";", self.w, ";", self.h, sep='')


s = Shape(5, 7)
s.draw()

c = Circle(120, 40, 30)
c.draw()

r = Rectangle(0, 0, 35, 1)
r.x = 35
r.draw()

s.printXY()
c.printXY()
r.printXY()
