from typing import List

from src.model.AbstractUser import AbstractUser


class SimpleUser(AbstractUser):
    def __init__(self, card_number: int, telegram_id: int = None):
        self.login = card_number
        self.password = card_number
        self.credentials = ["user", "student"]
        self.telegram_id = telegram_id
        # Номер зачётки
        self.card_number = card_number

    def get_login(self) -> str:
        return str(self.login)

    def get_password(self) -> str:
        return str(self.password)

    def get_credentials(self) -> List[str]:
        return self.credentials

    def get_telegram_id(self) -> int:
        return self.telegram_id
