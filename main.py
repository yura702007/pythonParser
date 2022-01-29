from pprint import pprint

import requests
from bs4 import BeautifulSoup
from fake_ua import header

URL = 'https://www.avito.ru/moskva/telefony/mobilnye_telefony/samsung-ASgBAgICAkS0wA2crzmwwQ2I_Dc?p='
FIELD_NAMES = ('title', 'price', 'metro', 'url')


def get_html(url=URL):
    r = requests.get(url, headers=header)
    return r.text


def get_total_pages(html_code):
    soup = BeautifulSoup(html_code, 'lxml')
    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a', class_='pagination-page')[-1]
    total_pages = int(pages.get('href').split('=')[-1])
    return total_pages


def html_data(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    links = soup.find_all('div', class_='iva-item-content-rejJg')
    # title, price, metro, url
    for link in links:
        try:
            title = link.find('h3').text
        except:
            title = ''
        try:
            price = link.find('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').text
        except:
            price = ''
        try:
            metro = link.find('div', class_='geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL').text
        except:
            metro = ''
        try:
            url = 'https://www.avito.ru' + link.find('a').get('href')
        except:
            url = ''
        # print(f'{title} - title')
        # print(f'{price} - price')
        # print(f'{metro}')
        # print(f'{url} - url\n')


def main():
    # resp = get_html()
    # count_links = get_total_pages(resp) + 1
    for i in range(10, 12):
        gen_url = URL + str(i)
        page_html = get_html(gen_url)
        html_data(page_html)
        break


if __name__ == '__main__':
    main()
