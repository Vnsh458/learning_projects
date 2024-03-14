import csv
import json
import os.path

import requests, lxml
from bs4 import BeautifulSoup


def get_all_pages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
    }
    # response = requests.get(url=url, headers=headers)
    #
    # if not os.path.exists('data'):
    #     os.mkdir('data')
    #
    # with open('data/page_1.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)

    with open('data/page_1.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    pages_count = int(soup.find('div', class_="bx-pagination-container").find_all('a')[-2].text)

    for page in range(1, pages_count + 1):
        url = f'https://hoztorgr.ru/novye-postupleniya/?PAGEN_1={page}'

        resp = requests.get(url=url, headers=headers)

        with open(f'data/data_{page}.html', 'w', encoding='utf-8') as file:
            file.write(resp.text)

    return pages_count + 1


def collect_data(pages_count):

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(
            (
                "Артикул",
                "Название",
                "Цена",
                "URL"
            )
        )

    data = []
    for page in range(1, pages_count):
        with open(f'data/data_{page}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        cards = soup.find('div', class_='row').find_all('div', class_='col-6 col-md-3')

        for card in cards:
            articul = card.find('span', class_="product-item__artnum product-item__artnum--card").text.lstrip('Арт: ')
            name = card.find('div', class_="product-item-title").text.strip()
            price = card.find('span', class_="product-item-price-current").text.strip()
            url = f"https://hoztorgr.ru{card.find('a', class_='product-item-image-wrapper').get('href')}"

            data.append(
                {
                    'Article': articul,
                    'Name': name,
                    'Price': price,
                    'URL': url
                }
            )

            with open('data.csv', 'a', encoding='cp1251', newline='', errors='ignore') as file:
                writer = csv.writer(file, delimiter=';')

                writer.writerow(
                    (
                        articul,
                        name,
                        price,
                        url
                    )
                )

        print(f'[INFO] Обработана страница {page}/{pages_count - 1}')

    with open('data.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages = get_all_pages('https://hoztorgr.ru/novye-postupleniya/')
    collect_data(pages)


if __name__ == '__main__':
    main()