import requests
import datetime


def get_data(city):
    key = ''
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

    request = requests.get(url).json()

    temp = request["main"]["temp"]
    temp_fells = request["main"]["feels_like"]
    humidity = request["main"]["humidity"]
    wind_speed = request["wind"]["speed"]
    sun_set = datetime.datetime.fromtimestamp(request["sys"]["sunset"])
    cloudy = request["clouds"]["all"]

    return temp, temp_fells, humidity, wind_speed, sun_set, cloudy


def eng_name(name):
    en_name = ''
    alfabet = {"А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "ZH", "З": "Z", "И": "I",
               "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T",
               "У": "U", "Ф": "F", "Х": "H", "Ц": "TS", "Ч": "CH", "Щ": "SHCH", "Ш": "SH", "Ь": "", "Ы": "Y", "Ъ": "IE",
               "Э": "E", "Ю": "IU", "Я": "IA"}

    for i in name:
        if i == " ":
            en_name += " "
        else:
            en_name += alfabet[i]
    return en_name.title()


def main():
    city = input('Enter your city: ')
    the_weater = get_data(city)


if __name__ == '__main__':
    main()
