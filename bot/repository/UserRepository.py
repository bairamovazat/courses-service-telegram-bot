from typing import List, Any

from django.core.exceptions import ObjectDoesNotExist


from courses.models import User


class UserRepository:

    def get_by_telegram_id(self, telegram_id: int):
        try:
            return User.objects.get(telegram_id=telegram_id)
        except ObjectDoesNotExist:
            return None

    def save(self, user: User):
        User.save(user)

    def delete(self, user: User):
        User.delete(user)