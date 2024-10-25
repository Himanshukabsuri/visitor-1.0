from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.loginPage, name='login'),
    path('dashboard/', views.dashboardPage, name='admin.dashboard'),
    
    path('visitorlist/',views.visitorlist,name="visitorlist"),
    path('addvisitor/',views.addvisitor,name="addvisitor"),
   path('update/<int:id>/', views.Editvisitor, name="editvisitor"),
   

]