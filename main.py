import telebot
from telebot import types
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot('TOKEN')

url1 = os.environ.get('URL1')
url2 = os.environ.get('URL2')
url3 = os.environ.get('URL3')
url4 = os.environ.get('URL4')
url5 = os.environ.get('URL5')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Эрмитаж")
    btn2 = types.KeyboardButton("Исаакиевский собор")
    btn3 = types.KeyboardButton("Летний сад")
    btn4 = types.KeyboardButton("Спас на крови")
    btn5 = types.KeyboardButton("Петропавловская крепость")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Эрмитаж":
        bot.send_message(message.chat.id, f"{url1}")

    elif message.text == "Исаакиевский собор":
        bot.send_message(message.chat.id, f"{url2}")

    elif message.text == "Летний сад":
        bot.send_message(message.chat.id, f"{url3}")
        
    elif message.text == "Спас на крови":
        bot.send_message(message.chat.id, f"{url4}")

    elif message.text == "Петропавловская крепость":
        bot.send_message(message.chat.id, f"{url5}")

    else:
        bot.send_message(message.chat.id, "Ой..")

bot.polling(none_stop=True)
