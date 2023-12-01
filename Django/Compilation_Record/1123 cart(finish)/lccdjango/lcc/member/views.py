from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse, HttpResponseRedirect
import hashlib


def login(request):
    msg = ""
    if "email" in request.POST:
        email = request.POST['email']
        pwd = request.POST['password']
        pwd = hashlib.sha3_256(pwd.encode('utf-8')).hexdigest()

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
    del request.session['cus_email']
    del request.session['isAlive']
    del request.session['lcc']
    # request.session.clear() 刪除全部的session
    response = HttpResponseRedirect('/') # 登出後導向首頁
    response.delete_cookie('UEmail') 
    return response


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
                                    address=address)

            msg = "註冊完成！"
        
        else:
            msg = "Email重複，請更新一個"
            
    return render(request, 'register.html', locals())
            
        
        
# 更改密碼        
def ChangePassword(request):
    # 在登入狀態 先判斷兩項session都存在
    if 'cus_email' in request.session and 'lcc' in request.session:
        msg = ''
        # 製作選單讓使用者輸入舊密碼跟新密碼
        if 'oldPwd' in request.POST:
            oldPwd = request.POST['oldPwd']
            newPwd = request.POST['newPwd']
            oldPwd = hashlib.sha3_256(oldPwd.encode('utf-8')).hexdigest()
            newPwd = hashlib.sha3_256(newPwd.encode('utf-8')).hexdigest()
            
            email = request.session['cus_email']
            # 判斷舊密碼是否存在於註冊的帳號當中
            obj = Customer.objects.fulter(email=email, password=oldPwd).count()
            if obj > 0:
                # 讀取帳號資料之後更新password欄位之後儲存
                user = Customer.objects.get(email=email)
                user.password = newPwd
                user.save()
                msg = '密碼更改成功'
            else:
                msg = '舊密碼錯誤，請重新輸入。'
    else:
        return HttpResponseRedirect('/login')


def updatePensonal(request):
    pass    