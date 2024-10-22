from django.shortcuts import render

def home(request):


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']  
        message = request.POST['message']
        send_email(name, email, message)
        return render(request, 'home.html', {'message': 'Email sent successfully'})
    


    return render(request, 'home.html')
