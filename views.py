#Made by me
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello reet")

def index(request):
    return render(request,'index.html')

