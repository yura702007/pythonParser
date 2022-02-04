import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://sitespy.ru/my-ip'


def get_html(url=URL):
    r = requests.get(url=url)
    return r.text


def get_ip(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip, '\n', ua)


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
    list_proxy = get_proxy()
    list_ua = get_ua()
    get_ip(get_html())


if __name__ == '__main__':
    main()
