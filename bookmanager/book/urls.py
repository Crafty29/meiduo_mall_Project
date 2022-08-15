from django.urls import path
from .views import index, register, json

urlpatterns = [
    path('index/', index),
    path('register/', register),
    path('json/', json),

]














