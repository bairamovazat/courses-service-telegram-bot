
from telegram import Bot, Update, User

from bot.controller.AbstractController import AbstractController
from bot.model.SimpleUser import SimpleUser
from bot.repository.RepositoryInMemory import RepositoryInMemory


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_card_number(text: str):
    command = text.split(" ")
    if len(command) < 2:
        return None

    if is_number(text.split(" ")[1]):
        return int(text.split(" ")[1])
    else:
        return None


class SimpleController(AbstractController):
    start_message = "Привет {0} !" \
                    "Меня зовут Бот обормот и я помогу тебе записаться на курсы!" \
                    "Думаю, сначала тебе нужно зареристрироваться." \
                    "Напиши /register 'номерЗачётки'"

    start_message_for_registered = "Снова привет {0}! Посмотри доступные тебе команды: /commands"

    unregistered_message = "Вы не зарегистрированы. Чтобы зарегистрироваться введите /register 'номерЗачётки'"

    def __init__(self, repository: RepositoryInMemory):
        self.handlers = {
            "start": self.start_controller,
            "register": self.register_controller,
            "unregister": self.unregister_controller,
            "commands": self.commands_controller,
            "profile": self.profile_controller,
        }
        self.repository = repository

    def get_user_by_update(self, telegram_user: User):
        if telegram_user is None or telegram_user.id is None:
            return None

        return self.repository.get_user_by_telegram_id(telegram_user.id)

    def get_handlers(self):
        return self.handlers

    def start_controller(self, bot: Bot, update: Update):
        telegram_user = update.effective_user
        user = self.get_user_by_update(telegram_user)

        if user is None:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=SimpleController.start_message.format(telegram_user.name)
            )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=SimpleController.start_message_for_registered.format(telegram_user.name)
            )

    def register_controller(self, bot: Bot, update: Update):
        telegram_user = update.effective_user
        user = self.get_user_by_update(telegram_user)

        if user is None:
            command_param = update.message.text.split(" ")
            if len(command_param) < 2:
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text="Чтобы зарегистрироваться введите /register 'номерЗачётки'."
                )
                return
            number = get_card_number(update.message.text)

            if number is None:
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text="Номер зачётки неверный!"
                )
                return

            new_user = SimpleUser(card_number=number, telegram_id=telegram_user.id)
            self.repository.create_user(new_user)

            bot.send_message(
                chat_id=update.message.chat_id,
                text="Успешно зарегистрированы!\n"
                     "Посмотреть все команды: /commands"
            )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="Вы уже зарегистрированы!"
            )

    def unregister_controller(self, bot: Bot, update: Update):
        telegram_user = update.effective_user
        user = self.get_user_by_update(telegram_user)

        if user is None:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=SimpleController.unregistered_message
            )

        else:
            number = get_card_number(update.message.text)
            if number is None:
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text="Чтобы удалить себя из системы введите /unregister 'номер-зачётки'.\n"
                         "Номер зачётки можно узнать через /profile"
                )
                return
            self.repository.delete_user(user)

            bot.send_message(
                chat_id=update.message.chat_id,
                text="Успешно удалены!"
            )

    def profile_controller(self, bot: Bot, update: Update):
        telegram_user = update.effective_user
        user = self.get_user_by_update(telegram_user)

        if user is None:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=SimpleController.unregistered_message
            )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="Ваш профиль:\n"
                     "Номер зачётки: {0}\n"
                     "Успеваемость: Скоро будет\n"
                     "Имя: Скоро будет\n"
                     "Фамилия: Скоро будет\n"
                     "Группа: Скоро будет\n"
                    .format(user.card_number)
            )

    def commands_controller(self, bot: Bot, update: Update):
        telegram_user = update.effective_user
        user = self.get_user_by_update(telegram_user)

        if user is None:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="Все команды:\n"
                     "/start - информация о боте\n"
                     "/register - регистрация\n"
                     "/commands - все команды\n"
            )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="Все команды:\n"
                     "/start - информация о боте\n"
                     "/unregister - удаление из системы\n"
                     "/commands - все команды\n"
                     "/profile - ваш профиль\n"
            )
