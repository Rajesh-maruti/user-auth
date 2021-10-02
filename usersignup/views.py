from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from usersignup.serializer import UserSerialzer
from common_definations.HandleResponse import bad_request, success_creation


# Create your views here.

class signUp(APIView):
    def __init__(self) -> None:
        super().__init__()

    @csrf_exempt
    def post(self, request) -> HttpResponse:
        serializer = UserSerialzer(data=request.data)
        if(serializer.is_valid()):
            user_instance = serializer.save()
        else:
            return bad_request(serializer.errors)
        return success_creation({
            "message": 'User Created Successfully!',
            "id": user_instance.id
        })
