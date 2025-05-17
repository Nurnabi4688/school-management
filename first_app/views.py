from django.shortcuts import render,redirect
from . forms import RegisterForm
from .models import Register
# Create your views here.


def Signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=RegisterForm
    return render(request,'index.html',{'form':form})

def base(request):
    return render(request,'base.html')

def student_list(request):
    data=Register.objects.all()
    return render(request,'student_list.html',{'data':data})

def edit_student(request):
    return render (request,'edit_student.html')