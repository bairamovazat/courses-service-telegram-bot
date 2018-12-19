from django.http import HttpResponse
from bot.main import BootStarter

botStarter = BootStarter()
botStarter.start_bot()


def index(request):
    if not botStarter.is_run():
        botStarter.start_bot()
    return HttpResponse("Привет! Сейчас сервис запущен и ты можешь написать боту <a "
                        "href='https://t.me/courses_service_bot'>https://t.me/courses_service_bot</a>")
