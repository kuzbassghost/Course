handler = open('a.txt', 'w')  # Открытие файла на запись
handler.write('Michael 13.01.1975 \n Mary 21/10/2005')  # Запись в файл
handler.close()  # Закрытие файла

handler = open('a.txt', 'r')  # Открытие файла на чтение
print(handler.read(2))  # Считывание файла до позиции 2
print(handler.read())  # Чтение продолжения содкржимого файла

handler.seek(0)  # Установка метки для чтения файла
print(handler.read())  # Чтение содкржимого файла с метки

#handler.close()  # Закрытие файла

for line in handler:
    print(line)
    handler.close()

print('---------------------')

file = 'b.txt'

while True:
    print('1 - Записать файл, 2 - прочитать файл, 0 - Выход')
    inp = input("Введите команду: ")
    if inp == "0":
        exit(0)
    elif inp == "1":
        text = input("Введитестроку: ")
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif inp == "2":
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла не сущемтвует")
    else:
        print("Неизвестная команда")
