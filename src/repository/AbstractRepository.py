from abc import abstractmethod

from src.model.AbstractUser import AbstractUser


class AbstractRepository:

    @abstractmethod
    def get_user(self, login: str, password: str):
        pass

    @abstractmethod
    def create_user(self, user: AbstractUser):
        pass
