from typing import List, Any

from courses.models import User


class UserRepository:

    def get_user(self, telegram_id: int) -> User:
        return User.objects.get(telegram_id=telegram_id)

    def create_user(self, user: SimpleUser):
        self.users.append(user)

    def delete_user(self, user: SimpleUser):
        self.users.remove(user)
