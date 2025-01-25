import telebot

token = "7564462862:AAHHMw2wmj_MmiH6AJu39WcUIAORe3v2gDI"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def command_stop(message):
    bot.send_message(message.chat.id, 'команда Старт!')


@bot.message_handler(content_types=['text'])
def command_stop(message):
    mes = message.text + '\nДовжина повідомлення:' + str(len(message.text)) + 'cимвол'
    bot.send_message(message.chat.id, mes)


if __name__ == '__main__':
    bot.polling()




