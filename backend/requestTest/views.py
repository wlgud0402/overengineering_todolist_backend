from django.shortcuts import render, HttpResponse
import json


# Create your views here.


def request(request):
    body = request.body.decode('utf-8')
    data = json.loads(body)['data']
    print("요청들어옴", data)
    return HttpResponse("요청왓씁니다.")
