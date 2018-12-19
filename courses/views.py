from django.http import HttpResponse

from bot.main import BotStarter

botStarter = BotStarter()
botStarter.start_bot()

def index(request):
    return HttpResponse(
        "Привет! Можешь написать боту <a href='https://t.me/courses_service_bot'>https://t.me/courses_service_bot</a>")
