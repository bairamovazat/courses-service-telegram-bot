import os

from bot.controller.SimpleController import SimpleController
from bot.repository.UserRepository import UserRepository
from bot.service.TelegramBot import TelegramBot
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = "622712955:AAGGQ_k9Grd_eY-3onHLfshbAodUFH-2MgU"


class BootStarter:
    def __init__(self):
        self.bot = None

    def start_bot(self) -> TelegramBot:
        repository = UserRepository()
        controller = SimpleController(repository)
        self.bot = TelegramBot(token=token)
        logging.log(level=logging.INFO, msg="End bot")
        self.bot.load_command_handlers(controller.get_handlers())
        # HEROKU
        self.bot.start_polling()
        # LOCAL
        # self.bot.start_polling_local()
        return self.bot

    def is_run(self):
        return self.bot is not None


if __name__ == "__main__":
    botStarter = BootStarter()
    botStarter.start_bot()
