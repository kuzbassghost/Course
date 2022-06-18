class Circle:
    x = 0
    y = 0
    r = 0
    def __init__(self, x, y, r = 0):
        self.x = x
        self.y = y
        self.r = r
        if r == 0:
            print("Радиус не задан")

c = Circle(5, 7, 10)
print(c.x, " ; ", c.y, " ; ", c.r)
c.x = 10
print(c.x)

c1 = Circle(5, 20)
print(c1.x, " ; ", c1.y, " ; ", c1.r)