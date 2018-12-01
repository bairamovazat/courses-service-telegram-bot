from abc import abstractmethod


class AbstractController:

    @abstractmethod
    def get_handlers(self):
        pass
