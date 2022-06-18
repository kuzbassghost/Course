import subprocess
import io

sp= subprocess.Popen(('dir'), stdout=subprocess.PIPE, shell=True) # Устанавливается соединение
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866") # Получаем данные в буфер
s = ' '
while s:                  # Выводим данные
    s = out.readline()
    print(s)