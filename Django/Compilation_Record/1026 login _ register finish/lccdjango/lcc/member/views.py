from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse, HttpResponseRedirect
import hashlib


def login(request):
    msg = ""
    if "email" in request.POST:
        email = request.POST['email']
        pwd = request.POST['password']
        pwd = hashlib.sha_256(pwd.encode('utf-8')).hexdigest()

        obj = Customer.objects.filter(email=email, password=pwd).count()
        
        if obj > 0:
            # 寫session 驗證登入
            request.session['cus_email'] = email
            request.session['isAlive'] = True
            request.session['lcc'] = 'good'
                    
            # max_age 存活秒數
            response = HttpResponseRedirect('/')
            response.set_cookie('UEmail', email, max_age=1200)
            
            return response
    
        else:
            msg = "帳號或密碼錯誤"
            
            return render(request, 'login.html', locals())
    
    else:
        return render(request, 'login.html', locals())
    
    
def logout(request):
    pass


def register(request):
    msg = ""
    if "u_email" in request.POST:        
        u_name = request.POST['u_name']
        u_email = request.POST['u_email']
        pwd = request.POST['password']
        sex = request.POST['sex']
        mobile = request.POST['mobile']
        address = request.POST['address']
        birthday = request.POST['birthday']
        # 對密碼作加密
        pwd = hashlib.sha3_256(pwd.encode('utf-8')).hexdigest()
        
        obj = Customer.objects.filter(email=u_email).count()
        
        if obj == 0:
            Customer.objects.create(name=u_name, 
                                    password=pwd,
                                    sex=sex, 
                                    birthday=birthday, 
                                    email=u_email, 
                                    mobile=mobile,
                                    address=address                                    
                                    )
            msg = "註冊完成！"
        
        else:
            msg = "Email重複，請更新一個"
            
    return render(request, 'register.html', locals())
            
        
def changepassword(request):
    pass


def updatePensonal(request):
    pass    