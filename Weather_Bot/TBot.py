import telebot

from main import get_data, eng_name

token = "TOKEN"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def get_start_mes(mes):
    if mes.text == '/start':
        bot.send_message(mes.from_user.id,
                         text='Привет, я погода бот, рассказываю о погоде на данный момент в твоем городе')
        bot.send_message(mes.from_user.id, text='Введи свой город. (Пример: Moscow)')
    else:
        bot.send_message(mes.from_user.id, text='Введи свой город. (Пример: Moscow)')


@bot.message_handler(content_types='text')
def get_mes(mes):
    try:
        en_mes = eng_name(mes.text)
        the_weather = get_data(en_mes.text)

        bot.send_message(mes.from_user.id, text=f'Tемпература: {the_weather[0]}\nОщущается: {the_weather[1]}'
                                                f'\nВлажность: {the_weather[2]}\nСкорость ветра: {the_weather[3]}\n'
                                                f'Время заката: {the_weather[4]}\nОблачность: {the_weather[5]}')

    except:
        bot.send_message(mes.from_user.id, text='Извини я не нашел этого города')


bot.polling(none_stop=True)
