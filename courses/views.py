from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Привет! Сейчас сервис запущен и ты можешь написать боту <a "
                        "href='https://t.me/courses_service_bot'>https://t.me/courses_service_bot</a>")
