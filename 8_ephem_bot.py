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
    if planet == 'mars':
        constellation = ephem.constellation(ephem.Mars(datetime.date.today()))
    elif planet == 'venus':
        constellation = ephem.constellation(ephem.Venus(datetime.date.today()))
    elif planet == 'neptune':
        constellation = ephem.constellation(ephem.Neptune(datetime.date.today()))
    elif planet == 'jupiter':
        constellation = ephem.constellation(ephem.Jupiter(datetime.date.today()))
    elif planet == 'moon':
        constellation = ephem.constellation(ephem.Moon(datetime.date.today()))
    elif planet == 'pluto':
        constellation = ephem.constellation(ephem.Pluto(datetime.date.today()))
    elif planet == 'saturn':
        constellation = ephem.constellation(ephem.Saturn(datetime.date.today()))
    elif planet == 'mercury':
        constellation = ephem.constellation(ephem.Mercury(datetime.date.today()))
    elif planet == 'uranus':
        constellation = ephem.constellation(ephem.Uranus(datetime.date.today()))
    elif planet == 'sun':
        constellation = ephem.constellation(ephem.Sun(datetime.date.today()))
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
