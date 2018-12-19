from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "Привет! Можешь написать боту <a href='https://t.me/courses_service_bot'>https://t.me/courses_service_bot</a>")
