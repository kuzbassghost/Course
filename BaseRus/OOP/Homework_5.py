"""
1) Сделайте у класса из предыдущего упражнения закрытыми все его поля.
2) Добавьте методы get и set для всех полей. Поскольку полей всего 4, то должно быть 4 метода get и 4 метода set.
3) Убедитесь, что доступа к полям уже нет за пределами класса.
4) Проверьте работу методов get и set.
5) Сделайте закрытый метод printlog(), в котором с помощью функции print() выводите значение переданного параметра.
6) В методах get и set вызывайте метод printlog с параметром: «Запрошено свойство NAME» (для методов get) или
«Изменено свойство NAME» (для методов set). Вместо NAME должно быть подставлено имя соответствующего свойства.
"""


class Rectangle:
    __x = 0
    __y = 0
    __h = 0
    __w = 0

    def __init__(self, x, y, h, w):  # Конструктор класса
        self.__x = x
        self.__y = y
        self.__h = h
        self.__w = w

    def getX(self):
        print("Запрошено свойство" , " x")
        self.__printlog("Запрошено свойство" , " x")
        return self.__x

    def getY(self):
        self.__printlog("Запрошено свойство", " y")
        return self.__y

    def getH(self):
        self.__printlog("Запрошено свойство", " h")
        return self.__h

    def getW(self):
        self.__printlog("Запрошено свойство", " w")
        return self.__w

    def setX(self, x):
        self.__printlog("Изменено свойство", " x")
        self.__x = x

    def setY(self, y):
        self.__printlog("Изменено свойство", " y")
        self.__y = y

    def setH(self, h):
        self.__printlog("Изменено свойство", " h")
        self.__h = h

    def setW(self, w):
        self.__printlog("Изменено свойство", " w")
        self.__w = w

    def __printlog(self, str1, str2):
        print(str1, str2)



p = Rectangle (10, 30, 50, 20)
print(p.getX())
print(p.getY())
print(p.getH())
print(p.getW())
print(p.setX(40))

print(p.getX())