from django.db import models

from django.db import models

class Visitor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    status_choices=[
        ('check-in','check-in'),
        ('check-out','check-out')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    discription=models.CharField(max_length=1000,default="a")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    status=models.CharField(max_length=20,choices=status_choices,default='check-in')

    def __str__(self):
        return self.name
