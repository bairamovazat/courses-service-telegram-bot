from django.conf.urls import url

from bot.main import BotStarter
from . import views

botStarter = BotStarter()
urlpatterns = [
    url(r'', views.index),
]
