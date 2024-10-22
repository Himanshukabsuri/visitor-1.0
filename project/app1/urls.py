from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.loginPage, name='login'),
    path('dashboard/', views.dashboardPage, name='admin.dashboard'),
    path('Register/',views.RegisterPage,name="Register")
]