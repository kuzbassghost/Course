"""
1) Напишите программу, которая будет принимать числа от пользователя и суммировать их, пока он не напишет слово «sum».
2) Когда пользователь напишет слово «sum», должна быть выведена сумма всех чисел и начат процесс заново.
3) Если пользователь напишет «exit» или «quit», программа должна быть завершена.
"""

i=0
n=0
while i<10:
    print("Введите число")
    number = input()
    if number == 'sum':
        print("Cумма всех введеных чисел равна: ", n)
        n=0
        continue

    if number == "exit" or number == "quit":
        break

    n += int(number)
