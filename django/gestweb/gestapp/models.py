from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    course=models.CharField(max_length=200)
    batch=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Teachers(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=10)
    subject=models.CharField(max_length=200)
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.name

