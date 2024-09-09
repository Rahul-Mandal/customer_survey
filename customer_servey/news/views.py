from django.shortcuts import render
from .models import Articles
# Create your views here.
def home(request):
    articles = Articles.objects.all()
    return render(request, 'home.html', {'articles':articles})


