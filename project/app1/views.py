from django.shortcuts import render,HttpResponse

def loginPage(request):
    return render(request,'login.html')
  
def dashboardPage(request):
    return render(request,'dashboard.html')

def RegisterPage(request):
    return HttpResponse("hlw")