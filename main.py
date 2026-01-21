import telebot
from telebot import types
import os
import flask
from flask import Flask
from threading import Thread

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

url1 = os.environ.get('URL1')
url2 = os.environ.get('URL2')
url3 = os.environ.get('URL3')
url4 = os.environ.get('URL4')
url5 = os.environ.get('URL5')
url6 = os.environ.get('URL6')
url7 = os.environ.get('URL7')
url8 = os.environ.get('URL8')
url9 = os.environ.get('URL9')
url10 = os.environ.get('URL10')
url11 = os.environ.get('URL11')
url12 = os.environ.get('URL12')
url13 = os.environ.get('URL13')
url14 = os.environ.get('URL14')
url15 = os.environ.get('URL15')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Эрмитаж")
    btn2 = types.KeyboardButton("Исаакиевский собор")
    btn3 = types.KeyboardButton("Летний сад")
    btn4 = types.KeyboardButton("Спас на крови")
    btn5 = types.KeyboardButton("Петропавловская крепость")
    btn6 = types.KeyboardButton("Михайловский замок")
    btn7 = types.KeyboardButton("Александровская колонна")
    btn8 = types.KeyboardButton("Соборная мечеть")
    btn9 = types.KeyboardButton("Кунсткамера")
    btn10 = types.KeyboardButton("Русский музей")
    btn11 = types.KeyboardButton("Смольный соборь")
    btn12 = types.KeyboardButton("Крейсер Аврора")
    btn13 = types.KeyboardButton("Музей Фаберже")
    btn14 = types.KeyboardButton("Казанский собор")
    btn15 = types.KeyboardButton("Мраморный дворец")

    markup.add(btn1, btn2, btn3, btn4, btn5)
    markup.add(btn6, btn7, btn8, btn9, btn10)
    markup.add(btn11, btn12, btn13, btn14, btn15)

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

    elif message.text == "Михайловский замок":
        bot.send_message(message.chat.id, f"{url6}")

    elif message.text == "Александровская колонна":
        bot.send_message(message.chat.id, f"{url7}")

    elif message.text == "Соборная мечеть":
        bot.send_message(message.chat.id, f"{url8}")

    elif message.text == "Кунсткамера":
        bot.send_message(message.chat.id, f"{url9}")

    elif message.text == "Русский музей":
        bot.send_message(message.chat.id, f"{url10}")

    elif message.text == "Смольный соборь":
        bot.send_message(message.chat.id, f"{url11}")

    elif message.text == "Крейсер Аврора":
        bot.send_message(message.chat.id, f"{url12}")

    elif message.text == "Музей Фаберже":
        bot.send_message(message.chat.id, f"{url13}")

    elif message.text == "Казанский собор":
        bot.send_message(message.chat.id, f"{url14}")

    elif message.text == "Мраморный дворец":
        bot.send_message(message.chat.id, f"{url15}")

    else:
        bot.send_message(message.chat.id, "Ой..\n\n Пропишите /start")

app = Flask('')

@app.route('/')
def home():
    return 'живу'

def run_http():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
        t = Thread(target=run_http)
        t.start()

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
