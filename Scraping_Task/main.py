from bs4 import BeautifulSoup
import requests, lxml


# 1st Task
headers = {
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
}

response = requests.get('https://www.oreilly.com/radar/', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

heads = soup.find_all('article', class_='homepage-card')

with open('scrap_ozon.html', 'w') as file:
    file.write(heads)
#
# for head in heads:
#     print(head.find('h2', class_="post-title").text)


# 2nd Task
