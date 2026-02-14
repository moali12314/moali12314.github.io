import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = telebot.TeleBot('8333491656:AAEX9f3mxLFoF-gdrieql_Hlxj4DOegYg_Y')  # Твой token

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Играть', web_app=WebAppInfo(url='https://your-url-here.com/index.html')))  # Замени URL
    bot.send_message(message.chat.id, 'Нажми кнопку для игры!', reply_markup=markup)

bot.polling()
