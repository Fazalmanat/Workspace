from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    std=Students.objects.all()
    return render(request,'index.html',{'std':std})

def home(request):
    std=Students.objects.all()
    if request.method=='POST':
        name=request.POST.get("name")
        address=request.POST.get("address")
        course=request.POST.get("course")
        batch=request.POST.get("batch")
        
        Students.objects.create(
            name=name,
            course=course,
            address=address,
            batch=batch
        )
        return redirect("home")
    return render(request,'home.html',{'std':std})