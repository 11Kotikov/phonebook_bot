import telebot
from my_token import my_token
from telebot import types
import user_interface as ui
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot=telebot.TeleBot(my_token)

example = ''

calc_keyboard = InlineKeyboardMarkup(row_width=1)
calc_keyboard.add(InlineKeyboardButton('New phone book (the old one will be deleted)', callback_data='0'),
                  InlineKeyboardButton('Show all contacts', callback_data='1'),
                  InlineKeyboardButton('Add a new contact', callback_data='2'),
                  InlineKeyboardButton('Find a contact', callback_data='3'),
                  InlineKeyboardButton('Delete a contact', callback_data='4'),
                  InlineKeyboardButton('Change the "NAME"', callback_data='5'),
                  InlineKeyboardButton('Change the "SURNAME"', callback_data='6'),
                  InlineKeyboardButton('Change the phone number', callback_data='7'),
                  InlineKeyboardButton('Export your phone book', callback_data='8'),
                  InlineKeyboardButton('Quit from the phone book', callback_data='9'))

@bot.message_handler(commands=['start'])
def calc_command(message: types.Message):
    bot.send_message(message.chat.id, 'This phone number book, hello dear "user_name"', reply_markup=calc_keyboard)



bot.polling(none_stop=True)