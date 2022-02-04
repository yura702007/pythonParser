import requests
from bs4 import BeautifulSoup
from fake_ua import header

URL = 'https://www.freeproxylists.net/ru/'


def get_html(url=URL):
    r = requests.get(url=url, headers=header)
    print(r.text)
    # return r.text


def parse_html(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    # tr_odd = soup.find_all('tr', class_='Odd')
    table = soup.find('table', class_='DataGrid')
    print(table)


def main():
    # parse_html(get_html())
    get_html()


if __name__ == '__main__':
    main()
