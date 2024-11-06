from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.loginPage, name='loginpage'),
    path('dashboard/', views.dashboardPage, name='admin.dashboard'),
    path('logoutpage/',views.logoutpage,name='logout'),
    path('visitorlist/',views.visitorlist,name="visitorlist"),
    path('addvisitor/',views.addvisitor,name="addvisitor"),
   path('update/<int:id>/', views.Editvisitor, name="editvisitor"),
   path('status/<int:id>/',views.st,name='st'),
   path('visitor/<int:id>/', views.visitor_detail, name='visitor_detail'),
   path('report/',views.report,name='report'),
   path('dashboard/', views.dashboardPage, name='admin.dashboard'),
   path('sub/', views.sub_view, name='sub_view'),
    path('sendemail/<int:id>/', views.sendemail, name='sendemail'),
]