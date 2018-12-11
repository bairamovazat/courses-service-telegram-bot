from abc import abstractmethod


class AbstractUser:

    @abstractmethod
    def get_login(self) -> str:
        pass

    @abstractmethod
    def get_password(self) -> str:
        pass

    @abstractmethod
    def get_credentials(self) -> str:
        pass
