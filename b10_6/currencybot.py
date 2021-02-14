# Реализация Telegram-бота, который возвращает цену
# на определённое количество валюты (евро, доллар или рубль).
import telebot
from extensions import KEYS, ExchangeCurrencies, APIException

with open('token.txt', 'r') as config:
    TOKEN = config.readline()
  
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hello'])
def help(message: telebot.types.Message):
    text=f'Приветствую, {message.chat.first_name}!\n\
Начните общение с ботом с команды /start.'
    bot.reply_to(message, text)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text="""Справка доступна при вызове команд /start или /help.
Для работы с ботом надо ввести команду:
    <имя валюты, цену которой вы хотите узнать>
    <имя валюты, в которой надо узнать цену первой валюты>
    <количество первой валюты>
Названия валют вводятся прописными буквами, а количество цифрами и
разделяются пробелами, например:
    доллар рубль 100
Примеры команд для конвертации выводятся командой /examples.
Информация о доступных валютах выводится командой /values.
    """
    bot.send_message(message.chat.id, text)
 

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    values = ''
    for key in KEYS.keys():
        values += f'{key}\n'
    text = f'Доступные валюты:\n{values}\n\
(доллар=доллар США,\n\
вона=южнокорейская вона,\n\
фунт=британский фунт,\n\
франк=швейцарский франк,\n\
крона=чешская крона,\n\
рупия=индийская рупия,\n\
лира=турецкая лира,\n\
рэнд=южноафриканский рэнд)'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['examples'])
def examples(message: telebot.types.Message):
    text ="""Примеры доступных команд для конвертации валют:
    (100 долларов в рубли) -> доллар рубль 100
    (50 иен в юани) -> иена юань 50
    (200 евро в фунты) -> евро фунт 200
Информация о доступных валютах выводится командой /values.
При конвертации итоговая сумма округляется до целого числа!
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        query = message.text.split(' ')
        if len(query) != 3:
            raise APIException('Обратитесь к командам /help или /example.')
        base, quote, amount = query
    except APIException as e:
        bot.send_message(message.chat.id,
                         f'Ошибка ввода команды!\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id,
                         f'Не удалось обработать команду {e}!')
    else:
        total = ExchangeCurrencies.get_price(base, quote, amount)
        bot.reply_to(message, total)


bot.polling()
