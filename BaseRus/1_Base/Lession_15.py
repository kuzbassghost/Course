def sum (x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s

def sub (x, y):
    global result
    result = float(x) - float(y)


result = 0
isprint = False
x = input("Введите число 1:  ")
y = input("Введите число 2:  ")
print("Сумма равна:  ", sum(x, y))
sub(x, y)
print("Разность равна: ", result)
