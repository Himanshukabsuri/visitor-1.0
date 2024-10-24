from django.db import models

from django.db import models

class Visitor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')

    def __str__(self):
        return self.name
