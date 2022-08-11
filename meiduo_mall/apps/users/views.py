import re

from django.shortcuts import render

# Create your views here.
"""
需求分析：根据页面的功能（从上到下，从左到右），那些功能需要和后端配合完成
如何确定：弄些功能需要和后端进行交互？
         1. 经验
         2. 关注类似网址的相似功能
"""

"""
判断用户名是否重复的功能。
前端：  当用户输入用户名之后，失去焦点，发送一个axios(ajax)请求
后端：  
        请求：      接收用户名
        业务逻辑：  根据用户名查询数据库，如果查询数量等于0，说明没注册，1 --> 注册
        响应：      JSON  {code:0, count:0/1, errmsg:ok}
        路由：      GET   usernames/<username>/count/
步骤：
        1. 接收用户名
        2. 根据用户名查询数据库
        3. 返回响应
        
"""
from django.views import View
from .models import User
from django.http import JsonResponse


class UsrnameCountView(View):
    def get(self, request, username):
        # 1. 接收用户名，对用户名进行判断
        if not re.match('[a-zA-Z0-9_-]{5,20}', username):
            return JsonResponse({'code': 200, 'errmsg': '用户名不满足要求'})
        # 2. 根据用户名查询数据库
        count = User.objects.filter(username=username).count()
        # 3. 返回响应
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})




