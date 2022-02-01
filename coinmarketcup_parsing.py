# 1 парсер однопоточный
# 2 замер времени
# 3 multiprocessing парсинг
# 4 замер времени
# 5 экспорт в csv
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool

URL = 'https://coinmarketcap.com'
FIELD_NAMES = ('name', 'price')


def get_html(url=URL):
    resp = requests.get(url=url)
    return resp.text


def get_all_links(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    trs = soup.find('tbody').find_all('tr')
    links = []
    for tr in trs:
        link = URL + tr.find('a', class_='cmc-link').get('href')
        links.append(link)
    return links


def get_data(url):
    page = get_html(url)
    soup = BeautifulSoup(page, 'lxml')
    name = soup.find('h2', class_='sc-1q9q90x-0 jCInrl h1').text.strip()
    price = soup.find('div', class_='priceValue').text.strip()
    data = {'name': name, 'price': price}
    return data


def write_csv(lst):
    with open('crypto_many.csv', 'w', newline='', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for row in lst:
            writer.writerow(row)
            print(f"{row['name']} is parse")


def make_all(url):
    data = get_data(url=url)
    print(data)


def main():
    start = datetime.now()
    all_links = get_all_links(get_html())
    with Pool(40) as p:
        p.map(make_all, all_links)
    end = datetime.now()
    print(end - start)


if __name__ == '__main__':
    main()
