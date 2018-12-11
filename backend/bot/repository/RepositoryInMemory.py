from typing import List, Any

from bot.model.AbstractUser import AbstractUser
from bot.model.SimpleUser import SimpleUser
from bot.repository.AbstractRepository import AbstractRepository


class RepositoryInMemory(AbstractRepository):

    def __init__(self):
        self.users = []  # type: List[SimpleUser]

    def get_user(self, login: str, password: str):
        for user in self.users:
            if user.get_password() == password and user.get_login() == login:
                return user
        return None

    def get_user_by_telegram_id(self, telegram_id: int):
        for user in self.users:
            if user.get_telegram_id() == telegram_id:
                return user
        return None

    def create_user(self, user: SimpleUser):
        self.users.append(user)

    def delete_user(self, user: SimpleUser):
        self.users.remove(user)