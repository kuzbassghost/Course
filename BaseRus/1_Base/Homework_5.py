"""
1) Самостоятельно подумайте, чему будет равно следующее логическое выражение: True and (True or (False and True or False) and True or True != False)
2) Проверьте себя, выведя результат этого выражения с помощью функции print().
3) Самостоятельно подумайте, чему будет равно следующее логическое выражение: 15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18)
4) Проверьте себя, выведя результат данного выражения с помощью функции print().
"""

print("True and (True or (False and True or False) and True or True =", True and (True or (False and True or False) and True or True))

print("15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18) =", 15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))

print()
print("___________________________")

print("True and True =", True and True)
print("True and False =", True and False)
print("True or False =", True or False)
print("True or True =", True or True)

print()

print("False and True =", False and True)
print("False  and False =", False and False)
print("False  or False =", False or False)
print("False or True =", False or True)
