from django.contrib import admin
from django.urls import path
from usersignup.views import signUp
urlpatterns = [
    path('', signUp.as_view())
]
