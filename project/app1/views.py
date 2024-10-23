from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("name")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('admin.dashboard')
        else:
            return HttpResponse("enter the vaild password or email")
    return render(request,'login.html')

  
def dashboardPage(request):
    return render(request,'base.html')



def addvisitor(request):
    return render(request,'addvisitor.html')