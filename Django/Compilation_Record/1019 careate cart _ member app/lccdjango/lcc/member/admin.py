from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email')
admin.site.register(Customer, CustomerAdmin)