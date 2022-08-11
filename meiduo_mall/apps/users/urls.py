from django.urls import path
from .views import UsrnameCountView


urlpatterns = [
    # 判断用户名是否重复
    path('usernames/<username:username>/count/', UsrnameCountView.as_view()),

]