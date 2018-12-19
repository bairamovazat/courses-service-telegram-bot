from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=128)
    rec_book_number = models.CharField(max_length=128)
    is_teacher = models.BooleanField()
    telegram_id = models.IntegerField()
    password = models.CharField(max_length=128)
