"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import datetime
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

from settings import API_KEY


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    logging.info('command "Start" received')
    update.message.reply_text('Привет')

def answer_me(update, context):
    update.message.reply_text(update.message.text)

def planet_where(update, context):
    logging.info('command "Planet" received')
    planet = update.message.text.split()[1].lower()
    #Так действительно лучше, но не знаю куда тогда воткнуть if из задания ))
    constellation = ephem.constellation(getattr(ephem, planet.capitalize())(datetime.date.today()))
    update.message.reply_text(constellation)

def main():
    mybot = Updater(API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_where))
    dp.add_handler(MessageHandler(Filters.text, answer_me))

    logging.info('Start')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
