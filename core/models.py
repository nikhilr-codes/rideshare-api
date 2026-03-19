from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ride(models.Model):
    STATUS_CHOICES=[
        ('REQUESTED', 'Requested'),
        ('ACCEPTED', 'Accepted'),
        ('STARTED', 'Started'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    rider=models.ForeignKey(User, on_delete=models.CASCADE,related_name="rides")
    driver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="drives")
    pickup_location=models.CharField(max_length=200)
    dropoff_location=models.CharField(max_length=200)
    status =models.CharField(max_length=30,default="requested",choices=STATUS_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rider} - {self.status}"
