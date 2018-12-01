import os

from flask import Flask, request

from src.controller.SimpleController import SimpleController
from src.repository.RepositoryInMemory import RepositoryInMemory
from src.service.TelegramBot import TelegramBot
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = "622712955:AAGGQ_k9Grd_eY-3onHLfshbAodUFH-2MgU"

if __name__ == "__main__":
    server = Flask(__name__)


    @server.route("/токен бота", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://ссылка на приложение/токен вашего бота")
        return "!", 200


    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

    repository = RepositoryInMemory()

    controller = SimpleController(repository)
    logging.log(level=logging.INFO, msg="Start boot")
    bot = TelegramBot(token=token)
    logging.log(level=logging.INFO, msg="End bot")

    bot.load_command_handlers(controller.get_handlers())
    bot.start_polling()
