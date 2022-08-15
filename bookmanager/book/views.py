from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('index')


def register(request):
    data = request.POST
    print(data)

    return HttpResponse('OK')


def json(request):
    body = request.body
    print(body)

    body_str = body.decode()
    print(body_str)

    # {
    #     "name": "itcast",
    #     "age": "18"
    # }

    # json形式的字符串，可以转换为python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    # {'name': 'itcast', 'age': '18'}

    return HttpResponse('json')







