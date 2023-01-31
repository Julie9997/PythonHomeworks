# Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# Пример:
# привет приабвет ограбпв

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = '5814205308:AAEqPkqY4p9R9aZ1ZNN78z6rBTGbnagWSgY'

bot = Bot(token=token) 
updater = Updater(token=token)
dispatcher = updater.dispatcher 

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\nВведите строку и я удалю из нее все слова, содержащие "абв"') 

def deleting_words(update, context):
    text = update.message.text
    new_text = [i for i in text.split() if not 'абв' in i.lower()]
    if len(new_text) == 0:
        message = 'Пришлось удалить все слова'
    else:
        message = ' '.join(new_text)
    context.bot.send_message(update.effective_chat.id, message)   


start_handler = CommandHandler('start', start) 
deleting_words_handler = MessageHandler(Filters.text, deleting_words)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(deleting_words_handler)

updater.start_polling()
updater.idle()