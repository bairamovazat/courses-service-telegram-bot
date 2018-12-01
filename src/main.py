from src.controller.SimpleController import SimpleController
from src.repository.RepositoryInMemory import RepositoryInMemory
from src.service.TelegramBot import TelegramBot
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


if __name__ == "__main__":
    repository = RepositoryInMemory()

    controller = SimpleController(repository)

    bot = TelegramBot(token="622712955:AAGGQ_k9Grd_eY-3onHLfshbAodUFH-2MgU")

    bot.load_command_handlers(controller.get_handlers())
    bot.start_polling()
