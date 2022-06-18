list = [1, 2, 0 , 5]  # Создает массив
print(list)           # выводит  массив на экран
print(len(list))      # Возвращает длину массива
list.append(9)        # Добавляет 9 в конец массива
print(list)
list.extend([0, 1])   # Добавляет массив в конец массива
print(list)
list.insert(1, 5)     # Добавляет 5 по индексу 1
print(list)

print("-------------")
print(list.index(0))    # Выводит индекс нуля
print(list.index(0, 4)) # Выводит индекс нуля начиная с 4 индекса
print(list.count('a'))  # Выводит колличество символа а вмассиве
print(list.count(0))    # Выводит колличество 0 вмассиве

print("-------------")

list.reverse()        # Переворачивает содержимое массива
print(list)

print("-------------")

list.remove(0)        # Удаляет 0 из массива
print(list)
list.pop(3)           # Удаляет элемент массива с индексом 3
print(list)
list.clear()          # отчищает весь массив
print(list)

print("-------------")

list = [1, 3, 0, 5, 1]
list.sort()             # Сортировка массива по возрастанию
print(list)
print(list)
list.sort(reverse=True) # Сортировка массива по убыванию
print(list)


print("-------------")

# все операции со кортежем аналогично операциям со списками
t = tuple("Hello!")
print(t.index("e"))
print(t.count("1"))