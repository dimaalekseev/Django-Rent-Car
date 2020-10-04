from django.db import models
from datetime import datetime

class CarManager(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(blank=True)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    #email=models.EmailField()
    hire_date=models.DateTimeField(default=datetime.now, blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.name