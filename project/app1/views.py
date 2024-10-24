from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail
from .models import Visitor

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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        gender = request.POST.get("gender")
        visitor = Visitor(name=name, email=email, phone=phone, date=date, gender=gender)
        visitor.save()
        return redirect("visitorlist")

    return render(request, 'addvisitor.html')


def visitorlist(request):
    visitors=Visitor.objects.all()

    return render(request,'visitorlist.html',{'visitors':visitors})

def Editvisitor(request,id):
    visitor=Visitor.objects.get(id=id)
    if request.method == "POST":
        visitor.name = request.POST.get("name")
        visitor.email = request.POST.get("email")
        visitor.phone = request.POST.get("phone")
        
        visitor.gender = request.POST.get("gender")
        visitor.save()
    return render(request,'update.html',{'visitor':visitor})