import requests
from bs4 import BeautifulSoup
import csv
from random import choice

URL = 'https://sitespy.ru/my-ip'


def get_html(url=URL, user_agent=None, proxy=None):
    print(proxy)
    r = requests.get(url=url, headers=user_agent, proxies=proxy)
    return r.text


def get_ip(html_text):
    print('Proxy & User-Agent')
    soup = BeautifulSoup(html_text, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip, '\n', ua)
    print('=' * 200)


def get_proxy():
    lst = []
    with open('proxy_list.csv', 'r', newline='', encoding='utf8') as file:
        reader = csv.DictReader(file, fieldnames=('ip', 'port'))
        for row in reader:
            lst.append(row)
    return lst[1:]


def get_ua():
    lst = []
    with open('user_agents.txt', 'r', encoding='utf8') as file:
        for line in file:
            lst.append(line.strip())
    return lst


def main():
    get_ip(get_html())
    list_proxy = get_proxy()
    list_ua = get_ua()
    for item in list_proxy:
        proxy = {'http': f'http://{item["ip"]}:{item["port"]}'}
        ua = {'User-Agent': choice(list_ua)}
        html_text = get_html(user_agent=ua, proxy=proxy)
        get_ip(html_text=html_text)


if __name__ == '__main__':
    main()
