import requests
from bs4 import BeautifulSoup

URL = 'https://sitespy.ru/my-ip'


def get_html(url=URL):
    r = requests.get(url=url)
    return r.text


def get_ip(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    ip = soup.find('span', class_='ip').text
    print(ip)


def main():
    get_ip(get_html())


if __name__ == '__main__':
    main()
