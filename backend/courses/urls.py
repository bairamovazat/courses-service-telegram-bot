import logging

from django.conf.urls import url
from . import views
from bot.controller.SimpleController import SimpleController
from bot.repository.RepositoryInMemory import RepositoryInMemory
from bot.service.TelegramBot import TelegramBot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = "622712955:AAGGQ_k9Grd_eY-3onHLfshbAodUFH-2MgU"


def init_telegram_bot():
    repository = RepositoryInMemory()
    controller = SimpleController(repository)
    bot = TelegramBot(token=token)
    logging.log(level=logging.INFO, msg="End bot")
    bot.load_command_handlers(controller.get_handlers())
    bot.start_polling()


urlpatterns = [

]


init_telegram_bot()