print("Введите 0 или 1 или 2: ")
a = input()
if a == "0":
    print("Вы ввели 0")
    print("0<10")
elif a == "1":
    print("Вы ввели 1")
elif a == "2":
    print("Вы ввели 2")
else:
    print("Не корректный ввод")

cond = a == 1 or a == 2 or a == 3

if cond:
    x = 1
else:
    x = 3

print("x = ", x)

x = 1 if cond else 3 # Сокрвщенная форма  if. Аналогично строкам 15-18.
print("x = ", x)