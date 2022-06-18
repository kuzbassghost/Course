print("Добропожаловать в наш модуль")

def getmax(*numbers):
    max = numbers[0]
    for n in numbers:
        if n > max:
            max = n
    return max

def getmin(*numbers):
    min = numbers[0]
    for n in numbers:
        if n < min:
            min = n
    return min

def bigsum(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum