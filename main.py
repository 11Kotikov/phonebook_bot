import telebot
from my_token import my_token
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#import my modules
import new_phone_book as newbook
import user_interface as ui
import contact_searching as cs
bot=telebot.TeleBot(my_token)

# example = ''

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
def greatings(message: types.Message):
    bot.send_message(message.chat.id, 'This phone number book, hello dear "user_name"', reply_markup=calc_keyboard)

@bot.callback_query_handler(lambda callback: callback.data)
def control_system (callback: types.CallbackQuery):
    if callback.data == '0':
        newbook.new_clear_book()
        bot.edit_message_text(f'You created a new clear book!', callback.message.chat.id, callback.message.id,
                        reply_markup=calc_keyboard)
    elif callback.data == '1':
        get_state = cs.open_full_book()
        if get_state == 0:
            bot.edit_message_text(f'Your book is empty!', callback.message.chat.id, callback.message.id,
                              reply_markup=calc_keyboard)
        else:
            with open('phone_book.csv') as pb:
                while True:
                    lines = pb.readline()
                    if not lines:
                        break
                    bot.send_message(callback.message.chat.id, lines.strip())
                    # bot.edit_message_text(f'{lines.strip()}', callback.message.chat.id, callback.message.id,
                              #reply_markup=calc_keyboard)
    # elif callback.data == '1':
    # elif callback.data == '1':
    # elif callback.data == '1':
    # elif callback.data == '1':
    # elif callback.data == '1':
    # elif callback.data == '1':
    # elif callback.data == '1':
    # else callback.data == '1':    


bot.polling(none_stop=True)