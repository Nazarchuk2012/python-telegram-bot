import telebot
from telebot import types
from urllib3 import request

from main import bot_message_text

token = "7087428460:AAFDIVBjoIcpji4UczvKW1jYXED3D6kaMug"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def  say_number(message):
    if message.text == '1':
        request = 'Один'
    elif message.text == '2':
        request = 'два'
    elif message.text == '3':
        request = 'три'
    elif message.text == '4':
        request = 'чотири'
    elif message.text == '5':
        request = 'Пять'
    else:
        request = 'Відповідь'

    bot.send_message(message.chat.id, request)


if __name__ == '__main__':
    bot.polling()







