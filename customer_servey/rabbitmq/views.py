from django.shortcuts import render
from django.http import HttpResponse
from .rabitmq import publish_message
# Create your views here.

def rab_index(request):
    publish_message('Hi this is a message')
    return HttpResponse('message published to rabitmq')
