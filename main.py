from telebot import TeleBot
from telebot.types import Message

BOT_TOKEN = 'YOUR BOT TOKEN'
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, "Instagram havolani yuboring!!!",
                     reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['text'])
def get_instagram_post_link(message: Message):
    from need_functions import instagram_downloader_func
    chat_id = message.chat.id
    bot.send_message(chat_id, "Havola olindi!\nBiroz kuting!")
    if instagram_downloader_func(message.text, chat_id=chat_id):
        text = "Ma'lumot yuklandi✅"
    else:
        text = "Ma'lumot yuklanmadi❌"
    bot.send_message(chat_id, text)


@bot.message_handler(content_types=['photo', 'audio', 'document', 'sticker', 'video', 'voice'])
def other_messages(message: Message):
    bot.send_message(message.chat.id, "Faqat havola yuboring!", reply_to_message_id=message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()
