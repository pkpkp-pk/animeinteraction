import telebot

import output_format

def anime_search(key):

    TOKEN = '1455138895:AAH8gK7va5O0tRPIVaJT3a5d5RCLbodbBlQ' #Replace *TOKEN* to your telegram bot token. Example: 123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw

    bot = telebot.TeleBot(TOKEN)

    chat_id = key.chat.id
    file = open('anime_list.txt', 'r', encoding='utf-8')

    all_data = file.readlines()
    anime_amount = 200

    key = key.text.replace(' ', '').lower()

    counter = 0
    max_a = 5

    for anime in range(anime_amount):
        splitted_data = all_data[anime].split(' | ')
        searching_data = splitted_data[1].lower().replace(' ', '')

        if searching_data.find(key) == 0:
            bot.send_message(chat_id, output_format.get_output(int(splitted_data[0])))
            print(f'Bot sent message:\n{output_format.get_output(int(splitted_data[0]))}')
            counter += 1
            if counter == max_a:
                break
        
    if counter == 0:
        bot.send_message(chat_id, 'Anime not found')
        print('Bot sent message: Anime not found')

    file.close()
