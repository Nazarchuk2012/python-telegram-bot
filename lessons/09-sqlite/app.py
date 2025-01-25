import config
import telebot
import threading
import time
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

USER_CHAT_ID = '6018884509'

# === SQLITE3 ===============================
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

# Обробник текстових повідомлення
@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Бот Працює!')


if __name__ == "__main__":
    thread = threading.Thread(target=send_stupid_message)
    thread.start()
    # Запуск бота
    bot.infinity_polling()









