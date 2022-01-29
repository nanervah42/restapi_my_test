from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/clients/', UserList.as_view()),
    path('api/clients/<int:pk>/', UserDetail.as_view()),
]