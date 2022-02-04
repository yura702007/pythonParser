from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = 'https://free-proxy-list.net/'
FIELD_NAMES = ['IP Address', 'Port', 'Https']


def get_html(url=URL):
    r = requests.get(url)
    return r.text


def get_proxy(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    table_head = soup.find('thead').find_all('th')
    headers_tab = [tag.text for tag in table_head]
    proxy_lst = []
    table_body = soup.find('tbody').find_all('tr')
    for tr in table_body:
        td_text = [td.text for td in tr.find_all('td')]
        proxy_lst.append(dict(zip(headers_tab, td_text)))
    return proxy_lst


def to_string(dict_data):
    # TODO ДОПИСАТЬ ФУНЦИЮ
    pass


proxese = get_proxy(get_html())

if __name__ == '__main__':
    pprint(proxese)
