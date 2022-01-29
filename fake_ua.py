import requests
from fake_user_agent.main import user_agent

ua = user_agent()
ua = user_agent("chrome")
header = {'User-Agent': ua}

if __name__ == '__main__':
    print(header)
    my_page = requests.get('https://httpbin.org', headers=header)
    print(my_page.headers)
