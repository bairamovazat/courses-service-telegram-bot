import datetime
import os
from collections import Callable
from typing import Dict

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.request import Request


class TelegramBot:

    def __init__(self, token):
        # 170717443 - @bairamov_azat id
        self.token = token
        self.bot = telegram.Bot(token=self.token, request=Request(con_pool_size=8))
        self.updater = Updater(bot=self.bot)
        self.dispatcher = self.updater.dispatcher

    def init_handler(self):
        self.bot.send_message(
            chat_id=170717443,
            text="Я запустился. Время: " + str(datetime.datetime.now())
        )

    def load_command_handlers(self, kwargs_handlers: Dict[str, Callable]):
        for key, value in kwargs_handlers.items():
            self.load_command_handler(key, value)

    def load_message_handlers(self, *args_handlers):
        for value in args_handlers:
            self.load_message_handler(value)

    def load_command_handler(self, command, handler):
        self.dispatcher.add_handler(CommandHandler(command, handler))

    def load_message_handler(self, handler):
        self.dispatcher.add_handler(MessageHandler(Filters.text, handler))

    def start_polling(self):
        self.updater.start_webhook(listen="0.0.0.0",
                                   port=int(os.environ.get('PORT', '8443')),
                                   url_path=self.token)
        self.updater.bot.setWebhook("https://courses-service-telegram-bot.herokuapp.com/" + self.token)
        self.updater.idle()
        self.init_handler()

    def start_polling_local(self):
        self.updater.start_polling()
        self.init_handler()
