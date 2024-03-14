import json
import os

from bs4 import BeautifulSoup
import requests


def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
    }
    # response = requests.get(url, headers=headers)

    # if not os.path.exists("data"):
    #     os.mkdir("Page`s data")

    # with open('Page`s data/page_1.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)

    with open('Page`s data/page_1.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    cards = soup.find('div', class_='product-item-small-card').find_all('div', class_='col-6 col-md-3')

    data = []
    # prod_data = {}

    for card, i in zip(cards, range(0, len(cards))):
        prod_data = {}
        url = card.find('a', class_='product-item-image-wrapper').get('href')
        # response = requests.get(f'https://hoztorgr.ru/{url}', headers=headers)
        # with open(f'Page`s data/product_{i}.html', 'w', encoding='utf-8') as file:
        #     file.write(response.text)

        with open(f'Page`s data/product_{i+1}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        product_items = soup.find('ul', class_='product-spec').find_all('span', class_='product-title')
        product_infos = soup.find('ul', class_='product-spec').find_all('span', class_='product-info')

        data.append(prod_data)
        prod_data.clear()

        for item, info in zip(product_items, product_infos):
            # print(f'{item.text}: {str(info.text).strip()}')
            prod_data[item.text] = str(info.text).strip()

    # with open("data.json", 'a') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    get_data('https://hoztorgr.ru/special_offer/')


if __name__ == '__main__':
    main()
