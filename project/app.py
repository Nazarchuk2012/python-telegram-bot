from telebot.apihelper import delete_chat_sticker_set

import config
import telebot
import threading
import time
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

USER_CHAT_ID = '6018884509'

# === SQLITE3 =================================================================
db = sqlite3.connect('notebook.db')
cursor = db.cursor()


#
cursor.execute('''CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    name TEXT DEFAULT 'Unknow',
    email TEXT DEFAULT '',
    role INTEGER DEFAULT 0,
    deleted INTEGER DEFAULT 1
    )''')
db.commit()

# === FUNCTIONS =============================
def send_stupid_message():
    while True:
        bot.send_message(USER_CHAT_ID, 'Дурненьке повідомлення')
        time.sleep(234235345)

# === HANDLER ===============================

start - підписка
add - додати
edit - редагувати
del - видалити
all - показати всі
day - показати за день
end - відписатися

# Обробник текстових повідомлення
@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'all', 'day', 'end'])
def handler_text_message(message):
    if '/start' == message.text:
        pass
    elif '/add' == message.text:
        pass
    elif '/edit' == message.text:
        pass
    elif '/del' == message.text:
        pass
    elif '/all' == message.text:
        pass
    elif '/day' == message.text:
        pass
    elif '/end' == message.text:
        pass


#Обробник текстових повідомлення
@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Бот Працює! ' + str(message.chat.id))


if __name__ == "__main__":
    #thread = threading.Thread(target=send_stupid_message)
    #thread.start()
    # Запуск бота
    bot.infinity_polling()









