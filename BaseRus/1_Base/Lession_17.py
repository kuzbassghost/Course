try:
    a= float("abs")
except ValueError:
    print("Невозможно привести к числу")

while True:
    a = input("Введите положительное число")
    try:
        a = float(a)
        if a<0:
            raise Exception ("Число не положительное")
    except ValueError:
        print("Невозможно привести к числу")
    except Exception as exp:
        print(exp)
    else:
        print("Спасибо закорректный ввод")
    finally:
        print("В любом случаи завершаем программу")
        exit(0)