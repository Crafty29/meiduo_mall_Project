from django.db import models

# Create your models here.
# 1. 自己定义模型
# 密码我们要加密，还要实现登陆的时候密码的验证
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=11, unique=True)

# 2. django 自带一个用户模型
# 这个用户模型有 密码的加密和密码的验证
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name



