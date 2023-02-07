from telegram import Bot
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from calculator import calculating
from logs import log

token = ''
bot = Bot(token=token) 
updater = Updater(token=token)
dispatcher = updater.dispatcher 

start_calc = 1
menu = 0

def start(update, context):
    start_keyboard = [['start']]
    markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(update.effective_chat.id,
                             'Привет, я бот-калькулятор рациональных чисел!')
    context.bot.send_message(update.effective_chat.id, 'Выбери действие:\n1. Вычислить выражение\n2.Выйти')
    return menu

def menu(update, context):
    data = update.message.text
    if data == '1':
        context.bot.send_message(update.effective_chat.id,
                                 'Я могу посчитать введенный пример\nТолько вводи с пробелами между цифрами и знаками.')
        return start_calc
    else:
        context.bot.send_message(update.effective_chat.id,
                                 'Пока!👋')
        return ConversationHandler.END

def calculator(update, context):
    user_id = update.effective_user.id
    username = update.effective_user.username
    if username:
        username = '@' + username

    data = update.message.text

    result = str(calculating(data))

    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')
    log(user_id, username, data, result)
    context.bot.send_message(update.effective_chat.id, 'Выбери действие:\n1. Вычислить выражение\n2.Выйти')
    return menu


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Пока!')


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
calculator_handler = MessageHandler(Filters.text, calculator) 
menu_handler = MessageHandler(Filters.text, menu) 

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start_calc: [calculator_handler],
                                   menu: [menu_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(calculator_handler)
dispatcher.add_handler(menu_handler)

updater.start_polling()
updater.idle()