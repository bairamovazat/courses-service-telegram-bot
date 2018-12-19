from django.http import HttpResponse
from bot.main import BootStarter


def index(request):
    return HttpResponse("Привет! Сейчас сервис запущен и ты можешь написать боту <a "
                        "href='https://t.me/courses_service_bot'>https://t.me/courses_service_bot</a>")
