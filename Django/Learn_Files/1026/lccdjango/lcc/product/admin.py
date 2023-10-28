from django.contrib import admin

# Register your models here.

from .models import Goods

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name','price','c_date')
    
    
admin.site.register(Goods,GoodsAdmin)    