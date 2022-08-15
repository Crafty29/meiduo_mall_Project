from django.urls import path
from .views import UsrnameCountView, RegisterView, LoginView


urlpatterns = [
    # 判断用户名是否重复
    path('usernames/<username:username>/count/', UsrnameCountView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]