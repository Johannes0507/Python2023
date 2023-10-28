from django.shortcuts import render

import hashlib

from .models import Customer

from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


def login(request):
   
    msg = ""
    if "email" in request.POST:
        email = request.POST['email']
        pwd = request.POST['password']
        pwd = hashlib.sha3_256(pwd.encode('utf-8')).hexdigest()
        
        obj = Customer.objects.filter(email=email,password=pwd).count()
        
        if obj > 0 :
            
            request.session['cusEmail'] = email
            request.session['isAlive'] = True
            request.session['lcc'] = 'good'
            
            
            #Redirect 
            response = HttpResponseRedirect('/')
            
            response.set_cookie('UEmail',email,max_age=1200)
            
            return response
        else:
            msg ="user or password fail"
            return render(request,'login.html',locals())
    
    else:
         return render(request,'login.html',locals())
        
        
   


def logout(request):
    pass


def register(request):
    
    msg = ""
    
    if "uEmail" in request.POST:
        
        uName = request.POST['uName']
        uEmail = request.POST['uEmail']
        pwd = request.POST['password']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        mobile = request.POST['mobile']
        address = request.POST['address']
        
        #
        pwd = hashlib.sha3_256(pwd.encode('utf-8')).hexdigest()
        
        obj = Customer.objects.filter(email=uEmail).count()
        
        if obj == 0:
            Customer.objects.create(name=uName,sex=sex,birthday=birthday,email=uEmail,mobile=mobile,address=address,password=pwd)
            msg = "Register Success"
        else:
            msg = "try again"
            
    return render(request,'register.html',locals())        
            
        
        
        
        
    
    

    