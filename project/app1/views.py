from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail
from .models import Visitor
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


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
@login_required
def dashboardPage(request):
    return render(request,'base.html')


@login_required
def addvisitor(request):
    today=timezone.now().date()
    todayvisitor=Visitor.objects.filter(date=today)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        discriptions=request.POST.get("Discriptions")
        gender = request.POST.get("gender")
        visitor = Visitor(name=name, email=email, phone=phone, discription=discriptions, gender=gender)
        visitor.save()
        
        return redirect("addvisitor")
        

    return render(request, 'addvisitor.html',{'todayvisitor':todayvisitor})


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

def  st(request,id):
    visitor=Visitor.objects.get(id=id)
    
    # print(visitor.status)
    if visitor.status=='check-in':
        visitor.status="check-out"
        
    visitor.save()
    
    return redirect('addvisitor')
