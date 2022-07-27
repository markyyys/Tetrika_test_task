import requests
import lxml
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D1%83%D1%80%D0%B0%D0%B2%D0%B5%D0%B9-%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE%D0%B9#mw-pages"
page = requests.get(url).text
alphabet = [('А', 0), ('Б', 0), ('В', 0), ('Г', 0), ('Д', 0), ('Е', 0), ('Ё', 0), ('Ж', 0), ('З', 0), ('И', 0),
                ('Й', 0), ('К', 0), ('Л', 0), ('М', 0), ('Н', 0), ('О', 0), ('П', 0), ('Р', 0), ('С', 0), ('Т', 0),
                ('У', 0), ('Ф', 0), ('Х', 0), ('Ц', 0), ('Ч', 0), ('Ш', 0), ('Щ', 0), ('Ъ', 0), ('Ы', 0), ('Ь', 0),
                ('Э', 0), ('Ю', 0), ('Я', 0)]
loop = True
while loop:
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
    for name in names:
        for i, a in enumerate(alphabet):
            if str(name.text)[0] == a[0]:
                alphabet[i] = (a[0], a[1] + 1)
        if name.text == "Ящурки":
            loop = False
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text

for a in alphabet:
    print(f"{a[0]}: {a[1]}")