from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail
from .models import Visitor
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print(f"User {username} authenticated successfully.")  # This should now print
            return redirect('admin.dashboard')
        
    
    return render(request, 'login.html')

@login_required
def dashboardPage(request):
    return render(request,'dashboard.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')



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
        messages.success(request, 'Visitor successfully created!')
        
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

def st(request, id):
    visitor = Visitor.objects.get(id=id)
    
    if visitor.status == 'check-in':
        visitor.status = "check-out"
        visitor.ctime = timezone.now()  
    
    visitor.save()
    messages.success(request, "Visitor successfully checked out")
    
    # Redirect to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'addvisitor'))

def visitor_detail(request, id):
    visitor = Visitor.objects.get(id=id)
    return render(request, 'visitor_detail.html', {'visitor': visitor})

def report(request):
    today = timezone.now().date()
    visitor = Visitor.objects.all()
    visitor_count = visitor.count()
    visitors_this_month = visitor.filter(date__month=today.month, date__year=today.year).count()
   
    
    # Retrieve search and filter values
    search = request.GET.get('search')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    selected_gender = request.GET.get('gender')
    
    # Initialize visitor_date to None, so it doesn't show data initially
    visitor_date = visitor
    
    # Apply search filter if the search term is provided
    if search:
        visitor_date = visitor_date.filter(name__icontains=search)
    
    # Apply date filter if both dates are provided
    if start_date and end_date:
        visitor_date = visitor_date.filter(date__range=[start_date, end_date])
    
    # Apply gender filter if a gender is selected
    if selected_gender:
        visitor_date = visitor_date.filter(gender=selected_gender)

    return render(request, 'report.html', {
        'visitors': visitor,
        'visitor_count': visitor_count,
        'start_date': start_date,
        'end_date': end_date,
        'selected_gender': selected_gender,
        'visitor_date': visitor_date,
        'visitors_this_month': visitors_this_month,
        'search': search
    })
import matplotlib.pyplot as plt
import io
import base64

@login_required
def dashboardPage(request):
    total_visitors = Visitor.objects.all().count()
    checked_in = Visitor.objects.filter(status='check-in').count()
    checked_out = Visitor.objects.filter(status='check-out').count()
    today = timezone.now().date()
    today_visit = Visitor.objects.filter(date=today).count()

    # Create a pie chart for checked-in and checked-out visitors
    pie_labels = ['Checked In', 'Checked Out']
    pie_values = [checked_in, checked_out]

    plt.figure(figsize=(8, 8))
    plt.pie(pie_values, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
    plt.title('Check-in vs Check-out Visitors')

    # Save the pie chart to a BytesIO object
    buf_pie = io.BytesIO()
    plt.savefig(buf_pie, format='png')
    plt.close()
    buf_pie.seek(0)

    # Encode the pie chart image to base64
    pie_image = base64.b64encode(buf_pie.read()).decode('utf-8')

    # Create a bar chart for total visitors, checked-in, checked-out, and today's visitors
    bar_labels = ['Total Visitors', 'Checked In', 'Checked Out', 'Today\'s Visitors']
    bar_values = [total_visitors, checked_in, checked_out, today_visit]

    plt.figure(figsize=(5, 5))
    plt.bar(bar_labels, bar_values, color=['blue', 'green', 'orange', 'red'])
    plt.title('Visitor Statistics')
    plt.xlabel('Categories')
    plt.ylabel('Number of Visitors')

    # Save the bar chart to a BytesIO object
    buf_bar = io.BytesIO()
    plt.savefig(buf_bar, format='png')
    plt.close()
    buf_bar.seek(0)

    # Encode the bar chart image to base64
    bar_image = base64.b64encode(buf_bar.read()).decode('utf-8')

    return render(request, 'dashboard.html', {
        'total_visitors': total_visitors,
        'checked_in': checked_in,
        'checked_out': checked_out,
        'today_visit': today_visit,
        'pie_image': pie_image,
        'bar_image': bar_image,
    })

