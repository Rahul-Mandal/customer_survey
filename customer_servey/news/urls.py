from django.urls import path
from news.views import *

urlpatterns = [
    path('home/', home, name='index'),
]