from bs4 import BeautifulSoup
import models
import main_parce

URL = ["http://bobruisk.by/gorod/sight/istkult/?curPos=", "http://bobruisk.by/gorod/sight/mestnie/?curPos="]

COUNT_PAGE = [9, 21]

HOST = 'http://bobruisk.by'

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36",
           "accept": "*/*"}

atrections = []


def get_src(html):
    soup = BeautifulSoup(html, 'lxml')
    l = soup.find('div', attrs={'class': 'col-xs-12 col-sm-8 col-md-8 col-lg-8'})
    h4 = [i.get_text(strip=True) for i in l.find_all('h4')]
    name, adres = '', ''
    if len(h4) == 1:
        name = h4[0].split('(')[0]
        adres = h4[0].split('(')[1][:len(h4[0].split('(')[1]) - 1]
    else:
        name = h4[0]
        adres = h4[len(h4) - 1][1:len(h4[len(h4) - 1]) - 1]
    content = l.find(attrs={'align': 'justify'}).get_text(strip=True)
    img = [HOST + i.get('src') for i in l.find_all('img')]
    atrections.append(models.Attractions(name, adres, content, img))


def parser(url, count_page):
    for i in range(1, count_page):
        main_parce.save_html(url, i)
        with open("index.html", 'r') as f:
            html = f.read()
        get_src(html)
        atrections[i-1].show()

for i in range(len(URL)):
    parser(URL[i], COUNT_PAGE[i])
