import  requests, bs4

url = "https://market.yandex.ru/catalog--elektronika/54440/list?text=%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D1%8B&cpa=1&hid=198119&srnum=1837&rs=eJwzYgpgBAABcwCG&was_redir=1&rt=9&onstock=0&local-offers-first=0"
r = requests.get(url)
r.encoding = 'UTF8'
print(r.text)

b = bs4.BeautifulSoup(r.text, "html.parser")

atitles = b.select("div._3Fff3 a")

titles = []

for a in atitles:
    print(a)
    titles.append(a.getText())

print(titles)

