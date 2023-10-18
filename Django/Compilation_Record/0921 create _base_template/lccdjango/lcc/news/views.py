from django.shortcuts import render

# Create your views here.

from .models import myNews


def news(request):
    
    data = myNews.objects.all()
    
    content = {'news_list':data}
    
    
    return  render(request,'news.html',content)