import telebot

token = "7564462862:AAHHMw2wmj_MmiH6AJu39WcUIAORe3v2gDI"
bot = telebot.TeleBot(token)


def isInt(value):
    try:
        return True
    finally:
        return False

@bot.message_handler(content_types=['text'])
def say_bot(message):

     if is

    with open('f2.txt', 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, "ок")


if __name__ == '__main__':
    bot.polling()



