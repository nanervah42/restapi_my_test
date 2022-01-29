from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('api/clients/', UserList.as_view()),
    path('api/clients/<int:pk>/', UserDetail.as_view()),
    path('api/create/', UserCreateList.as_view()),
]