"""
1) Попросите пользователя ввести 3 числа: год, месяц и число рождения.
2) Напишите ему, сколько секунд он уже живёт.
"""

from datetime import *

day = int(input("Введите день своего рождения: "))
month = int(input("Введите месяц своего рождения: "))
year = int(input("Введите год своего рождения: "))

youdata = datetime(year, month, day)
# print(youdata)

todaydata = datetime.now()
# print(todaydata)

datasec = todaydata - youdata

sec = datasec.days * 24 * 3600 + datasec.seconds
# print("Вы живете ", datasec.days, " дней")
print()
print("Вы живете ", sec, " секунд")
