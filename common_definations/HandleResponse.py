from django.http import JsonResponse
from django.http.response import HttpResponse
import json


def bad_request(message):
    print(message)
    return JsonResponse(status=400, data=message)


def success_creation(message):
    return HttpResponse(status=201, content=f'{message}')
