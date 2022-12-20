from django.shortcuts import render
from Student.models import Student


def view_info(request):
    stud_info = Student.objects.all()
    comp_info = Company.objects.all()
    return render(request,'info.html',{'stud' : stud_info,'comp' : comp_info})

def view_home(request):
    return render(request,'home.html',{})