s1 = "str_1"
print(len(s1)) # Выводит длина строки
print(s1[1])   # Выводит второй символ строки
print(s1[-1])  # Выводит последний символ строки
print(s1[-2])  # Выводит предпоследний символ строки
print(s1[1:3]) # Выводит символы строки начиная со второго символа в диапазоне 3 символов от начала строки

s1 = "abc\\xyz" # Скрывает наклонную черту
s2 = r"abc\xyz" # Скрывает наклонную черту второй вариант
print(s1)
print(s2)

print("-----------------")

a1 ="hello"
a2 = a1*3   # склеивает строки 3 раза
print(a1)
print(a2)

print(a1.find("l"))     # Индекс вхождения символа
print(a1.find("l", 3))  # Поиск индекса с указанной позиции

print(a1.isdigit()) # Является ли строка числом
print(a1.isalpha()) # Является ли строка символьной
print(a1.isupper()) # Является ли строка в верхнем регистре
print(a1.islower()) # Является ли строка в нижнем регистре

print("___________")
print(ord("a"))     # получает код заданного символа
print(chr(98))      # получает символ заданного кода

s1 = "       hello        "
print(s1)
print(s1.strip()) # вырезаетпробелы спереди и ссади

print("----------------")

s1 = "Здравствуйте, {0}, Вам {1} лет!" # Задает шаблон
print(s1.format('Alex', 30))           # Заполнение шаблона

s1 = "Здравствуйте, {name}, Вам {age} лет!"         # Задает шаблон
print(s1.format(name = 'Alex', age = 30))           # Заполнение шаблона

data = ('Alex', 30)                              # Передача картежа
s1 = "Здравствуйте, {0[0]}, Вам {0[1]} лет!"
print(s1.format(data))

s1 = "int: {0:d}; {0:b}" # Приведение числа к десятичному и двоичному форматам
print(s1.format(5))

s1 = "Round (150/47): (0:.3)" #Округление числа до 3 цифр
print(s1.format(150/47))
