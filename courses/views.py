from django.http import HttpResponse

from bot.main import BotStarter

bot = BotStarter()


def index(request):
    if not bot.is_run():
        bot.start_bot()
    return HttpResponse(
        "Привет! Можешь написать боту <a href='https://t.me/courses_service_bot'>https://t.me/courses_service_bot</a>")
