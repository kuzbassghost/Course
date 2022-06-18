import cgi, html
r = cgi.FieldStorage()

a = html.escape(r.getvalue("a", ""))
b = html.escape(r.getvalue("b", ""))

message = ""
result = ""

try:
    result = float(a) + float(b)
    result = "<p>Сумма чисел равна: " + str(result) + "</p>"
except ValueError:
    message = "<p style='color: red;'>Вывели не числа! </p>"


print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;'>")
print("<h1>Первая Web страница!</h1>")
print("<p>Какой-нибудь текст</p>")

print('''
<form name="form" style="magrin: 0 auto"; action="/cgi-bin/index.py" metod="post">
    <h2>Сложение чисел</h2>
    ''' + message +
    '''
    <label>Число 1</label>
    <input type="text" name="a" value="''' + a + '''" />
    <br />
    <br />
    <label>Число 2</label>
    <input type="text" name="b" value= "''' + b + '''"  />
    <br />
    <br />
    <input type="submit" value="Посчитать" />
    ''' + result +
    '''</form>''')
print(a)
print(b)

print("</body></html>")
