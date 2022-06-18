"""
1) Сделайте класс автомобиля из предыдущего упражнения абстрактным.
2) Сделайте метод движения у этого класса так же абстрактным.
3) Создайте ещё один дочерний класс от класса автомобиля для ещё какой-нибудь конкретной модели и реализуйте
   абстрактный метод движения.
"""

from abc import ABC, abstractmethod


class Auto(ABC):
    x = 0
    y = 0
    color = "None"

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def move(self):
        pass


class Toyota(Auto):
    model = "None"
    type = "None"

    def __init__(self, x, y, color, model, tape):
        Auto.__init__(self, x, y, color)
        self.model = model
        self.type = tape

    def move(self):
        print("Движение автомобиля ", self.model, " ", self.color, " цвета, типа ", self.type, " в точку ", self.x, ";",
              self.y, sep='')


class Nissan(Auto):
    model = "None"
    type = "None"

    def __init__(self, x, y, color, model, tape):
        Auto.__init__(self, x, y, color)
        self.model = model
        self.type = tape

    def move(self):
        print("Движение автомобиля в точку ", self.x, ";", self.y, " ", self.model, " ", self.color, " цвета, типа ",
              self.type, " в точку ", self.x, ";",
              self.y, sep='')



toyota = Toyota(45, 67, "Silver", "Toyota Corolla", "universal")
toyota.move()
nissan = Nissan(84, 20, "Silver", "Nissan Sany", "sedan")
nissan.move()
