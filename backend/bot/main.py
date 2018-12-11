import os

from bot.controller.SimpleController import SimpleController
from bot.repository.RepositoryInMemory import RepositoryInMemory
from bot.service.TelegramBot import TelegramBot
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = "622712955:AAGGQ_k9Grd_eY-3onHLfshbAodUFH-2MgU"

if __name__ == "__main__":
    repository = RepositoryInMemory()
    controller = SimpleController(repository)
    bot = TelegramBot(token=token)
    logging.log(level=logging.INFO, msg="End bot")
    bot.load_command_handlers(controller.get_handlers())
    bot.start_polling()
