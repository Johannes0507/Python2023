from django.db import models

# Create your models here.

class OrderModel(models.Model):
    subtotla = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    grandtotal = models.IntegerField(default=0)
    custome_name = models.CharField(max_length=50)
    custome_email = models.EmailField(max_length=50)
    custome_phone = models.CharField(max_length=50)
    custome_address = models.CharField(max_length=200)
    paytype = models.CharField(max_length=10)
    bankaccount = models.CharField(max_length=10, null=True)
    
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.custome_name
    

class DetailModel(models.Model):
    dorder = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    unitprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    dtotal = models.IntegerField(default=0)
    
    def __str__(self):
        return self.pname