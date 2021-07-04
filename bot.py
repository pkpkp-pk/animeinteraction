import random

import telebot

import output_format
import anime_parser.anime
import search

TOKEN = '1455138895:AAH8gK7va5O0tRPIVaJT3a5d5RCLbodbBlQ' #Replace *TOKEN* to your telegram bot token. Example: 123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def get_text_messages(message):

    chat_id = message.chat.id
    user_id = message.from_user.id
    anime_amount = 10500

    if message.text == 'Hello': #Test message

        bot.reply_to(message, 'Hello.')
        print('Bot sent message:', 'Hello')

    elif message.text == '/randomAnime':

        anime_num = random.randint(0, anime_amount)

        bot.send_message(chat_id, output_format.get_output(anime_num))
        print(f'Bot sent message:\n{output_format.get_output(anime_num)}')

    elif message.text == '/searchAnime':

        bot.send_message(chat_id, 'Enter Anime name:')
        bot.register_next_step_handler(message, search.anime_search)

    elif message.text == '/parse':
        if user_id == 123456789 or user_id == 987654321: #Only privileged users with id's 123456789 and 987654321 can use this command

            bot.send_message(chat_id, 'Parsing has been started...')
            print('Bot sent message: Parsing has been started...')
            bot.send_message(chat_id, anime_parser.anime.remaining_time(anime_amount, 7))
            print(f'Bot sent message: {anime_parser.anime.remaining_time(anime_amount, 7)}')
            anime_parser.anime.parse()
            bot.reply_to(message, 'Parsing is over')
            print('Bot sent message: Parsing is over')

        else:
            bot.reply_to(message, 'Access denied')
            print('Bot sent message: Access denied')
    

bot.polling(none_stop=True, interval=0)
