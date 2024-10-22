from django.shortcuts import render

def loginPage(request):
    return render(request,'login.html')
  
def dashboardPage(request):
    return render(request,'dashboard.html')
  