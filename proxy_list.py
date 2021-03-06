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


def get_proxies(dict_data):
    _proxy = []
    while dict_data:
        item = dict_data.pop(0)
        key = item['Protocol']
        value = f'{item["Protocol"]}://{item["IP Address"]}:{item["Port"]}'
        _proxy.append({key: value})
    return _proxy


def define_protocol(data):
    for item in data:
        t = item.pop('Https')
        if t == 'yes':
            item['Protocol'] = 'https'
        elif t == 'no':
            item['Protocol'] = 'http'
    return data


proxy_list = get_proxy(get_html())
proxy_list = define_protocol(proxy_list)
proxies = get_proxies(proxy_list)

if __name__ == '__main__':
    pprint(proxies)
