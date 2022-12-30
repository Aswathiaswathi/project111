from django.shortcuts import render,redirect
from .models import deptmodel,doctorsmodel,bookingmodel
from .forms import bookingform,signupform

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def booking(request):
    if request.method=="POST":
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"confirmation.html")
    form=bookingform()
    return render(request,"booking.html",{'form':form})

def doctors(request):
    doc=doctorsmodel.objects.all()
    return render(request,"doctors.html",{'doc':doc})

def department(request):
    dep=deptmodel.objects.all()
    return render(request,"department.html",{"dep":dep})

def contact(request):
    return render(request,"contact us.html")

def signup(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            redirect('signup.html')
        else:
            print("form is not valid")
    form=signupform()
    return render(request,'signup.html',{'form':form})


