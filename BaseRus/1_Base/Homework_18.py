"""
1) Откройте командную строку в своей системе.
2) Узнайте, с помощью какой команды можно получить текущую дату, используя команду help, либо документацию к своей ОС.
3) Напишите программу, которая выполняет эту команду и выводит результат с помощью функции print().
"""

import subprocess
import io

sp= subprocess.Popen(('date'), stdout=subprocess.PIPE, shell=True) # Устанавливается соединение
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866") # Получаем данные в буфер
s = ' '
while s:                  # Выводим данные
    s = out.readline()
    print(s)