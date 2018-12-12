from django.conf.urls import url
from . import views

from bot.main import start_bot

urlpatterns = [
    url(r'', views.index),
]

start_bot()
