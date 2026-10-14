from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    std=Students.objects.all()
    tcr=Teachers.objects.all()
    context={
        'std':std,
        'tcr':tcr
    }
    return render(request,'index.html',context)

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
def login(request):
    tcr=Teachers.objects.all()
    if request.method=='POST':
            name=request.POST.get("name")
            subject=request.POST.get("subject")
            code=request.POST.get("code")
            department=request.POST.get("department")
            
            Teachers.objects.create(
                name=name,
                code=code,
                subject=subject,
                department=department
            )
            return redirect("index")
    return render(request,'form.html',{'tcr':tcr})

def Update(request,id):
    std=get_object_or_404(Students,id=id)
    if request.method=='POST':
        std.name=request.POST.get("name")
        std.address=request.POST.get("address")
        std.course=request.POST.get("course")
        std.batch=request.POST.get("batch")
        std.save()
        return redirect("index")
    return render(request,'update.html')

def Delete(request,id):
    std=get_object_or_404(Students,id=id)
    if request.method=='POST':
        std.delete()
        return redirect("index")