from django.contrib import admin

# Register your models here.
from .models import OrderModel, DetailModel


admin.site.register(OrderModel)
admin.site.register(DetailModel)