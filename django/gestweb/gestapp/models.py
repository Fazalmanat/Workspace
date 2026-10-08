from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    course=models.CharField(max_length=200)
    batch=models.CharField(max_length=10)
    def __str__(self):
        return self.name