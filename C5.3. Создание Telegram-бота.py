# import telebot
#
# TOKEN = ""
#
# bot = telebot.TeleBot(TOKEN)
#
# bot.polling(none_stop=True)
#
# @bot.message_handler

import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['voice', ])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'У тебя очень красивый голос')
# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.


# @bot.message_handler(commands=['start', 'help'])
# def repeat(message: telebot.types.Message):
#     bot.reply_to(message, f'Приветствую, {message.chat.username}')

# def handle_start_help(message):
#     pass


# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")
#
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, '«Nice meme XDD»')


bot.polling(none_stop=True)

