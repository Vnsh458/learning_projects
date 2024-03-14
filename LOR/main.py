import requests

url_chapter = 'https://the-one-api.dev/v2/book/5cf58077b53e011a64671583/chapter'
url_character = 'https://the-one-api.dev/v2/character'
token = 'MBRk7RwUPc5CoyfquNgF'

res_chapter = requests.get(url_chapter).json()
res_character = requests.get(url_character, headers={'Authorization' : f'Bearer {token}'}).json()

def get_head(head_dict):
    chapter = len(head_dict['docs'])
    return chapter

def get_character(character_dict):
    character = len(character_dict['docs'])
    return character

print(f'Колическо глав в книге: {get_head(res_chapter)}\n'
      f'Количество персонажей: {get_character(res_character)}')