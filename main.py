from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/moskva/telefony/mobilnye_telefony/samsung-ASgBAgICAkS0wA2crzmwwQ2I_Dc?p='


def get_html(url=URL):
    r = requests.get(url)
    return r.text


def get_total_pages(html_code):
    soup = BeautifulSoup(html_code, 'lxml')
    pages = (
        soup.find(
            'div', class_='pagination-root-Ntd_O'
        ).find_all('span', class_='pagination-item-JJq_j')[-2].get('data-marker')
    )
    total_pages = int(pages.split('(')[-1].split(')')[0])
    return total_pages


def main():
    resp = get_html()
    get_total_pages(resp)
    count_links = get_total_pages(resp) + 1
    for i in range(1, count_links):
        gen_url = URL + str(i)
        print(gen_url)


if __name__ == '__main__':
    main()
