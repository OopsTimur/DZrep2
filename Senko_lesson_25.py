# Senko Timur (group_208)


import telebot
from telebot import types

Token = '6192818090:AAGQN4VguFWStbtgxnHE0MqDX7_f2kBwZDs'
bot = telebot.TeleBot(Token)


def new_keyboard():
    keyboard_1 = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    joke_btn = types.InlineKeyboardButton(text='Хочу анекдот', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    hello_btn = types.InlineKeyboardButton(text='Привет бот.', callback_data='5')
    farewell_btn = types.InlineKeyboardButton(text='Прощай бот.', callback_data='6')
    keyboard_1.add(drink_btn, eat_btn, joke_btn, sleep_btn, farewell_btn, hello_btn)
    return keyboard_1


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, 'Приветствую, чего желаете? ', reply_markup=new_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '1':
            img = 'https://www.zdorovieinfo.ru/wp-content/uploads/2020/08/shutterstock_326584550.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка воды',
                           reply_markup=new_keyboard())
        if call.data == '2':
            img = 'https://rare-gallery.com/uploads/posts/825950-Fast-food-Hamburger-Vegetables.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка еды', reply_markup=new_keyboard())
        if call.data == '3':
            txt = 'После 10 лет работы продавцом, Анастасия год проработала на скотобойне, чтобы как-то отдохнуть и ' \
                  'переключиться.'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=new_keyboard())
        if call.data == '4':
            txt = 'Держи снотворные, дед!'
            img = 'https://mon.medikforum.ru/uploads/posts/2019-09/1569848607_1569848657.jpg'
            bot.send_message(chat_id=call.message.chat.id, text=txt)
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка таблеток',
                           reply_markup=new_keyboard())
        if call.data == '5':
            txt = 'Привет, что вам нужно?'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=new_keyboard())
        if call.data == '6':
            txt = 'Удачи пользователь!'
            bot.send_message(chat_id=call.message.chat.id, text=txt, reply_markup=new_keyboard())


bot.polling(none_stop=True)
