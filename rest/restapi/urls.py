from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/clients/', UserList.as_view()),
]