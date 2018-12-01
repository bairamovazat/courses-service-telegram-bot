from collections import Callable
from typing import Dict

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.bot = telegram.Bot(token=self.token)
        self.updater = Updater(bot=self.bot)
        self.dispatcher = self.updater.dispatcher

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
        self.updater.start_polling()
