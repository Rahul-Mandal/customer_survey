"""customer_servey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import *
from rabbitmq.views import *

urlpatterns = [
    path('', index, name='index'),
    path('feedback/<id>', customer_feedback, name='customer_feedback'),
    path('admin/', admin.site.urls),
    path('thank-you/', thank_you, name='thank_you'),
    path('rab/', rab_index, name='rabindex'),
    path('student/', StudentApi.as_view()),
    path('login/', LoginApi.as_view()),
    path('', include('news.urls'))
]
