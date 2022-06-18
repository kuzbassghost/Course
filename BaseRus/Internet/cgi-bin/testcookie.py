import cgi, http.cookies, os

dict = {'red': 'Красный', 'green': 'Зеленый', 'orange': 'Ораньжевый'}

r = cgi.FieldStorage()
color = r.getvalue('color', 'white')

bg = 'background-color: {0};'
#bg = bg.format('green')

if dict.get(color):
    bg = bg.format(color)
    print("Set-cookie: color=" + color)
else:
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    color = cookie.get("color").value

print("Content-type: text/html; charset=utf-8")
print()
print("<html><head><title>Заголовок</title></head><body style='text-align: center;" + bg + "'>")
print("<h1>Test cookie!</h1>")
for key in dict:
    print("<h2><a href='?color=" + key + "'>" + dict[key] + "</a></h2>")
print(color)
print("</body></html>")
