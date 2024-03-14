import os.path
import requests
from bs4 import BeautifulSoup


def get_pages(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # if not os.path.exists('data'):
    #     os.mkdir('data')

    with open('data/head_page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    # with open('data/head_page.html', 'r', encoding='utf-8') as file:
    #     src = file.read()
    #
    # soup = BeautifulSoup(src, 'lxml')
    # pages_count = soup.find('div', class_='pagination-hidden-zHaij').find_all('a', class_='pagination-page').get('href')
    #
    # for i in range(1, 7):
    #     print(i)
    # # link = soup.find('div', class_='items-items-kAJAg').find_all('', class_='')


def main():
    get_pages('https://www.avito.ru/krasnoyarsk?q=легковые+шины')


if __name__ == '__main__':
    main()