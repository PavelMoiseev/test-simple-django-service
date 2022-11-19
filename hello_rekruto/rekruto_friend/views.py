from django.http import HttpResponse
import requests


def index(request):
    if request.method == 'GET':
        try:
           name = request.GET.get('name')
           message = request.GET.get('message')
        except Exception as e:
            return HttpResponse('Что-то не работает :(')

        return HttpResponse(f'Hello {name}! {message}!')
