from django.shortcuts import render

# Create your views here.

from .models import myNews

# Paginator -> 控制 EmtyPage -> 分頁空白時的操作 PageNotAnInteger
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news(request):
    
    data = myNews.objects.all()
    
    
    # 分頁
        
    paginator = Paginator(data, 15) # 15比為一個頁
    
    page = request.GET.get('page')
    
    content = {'news_list':data}

    
    return  render(request,'news.html',content)