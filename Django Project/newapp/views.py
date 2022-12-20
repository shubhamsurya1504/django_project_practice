from django.shortcuts import render,redirect
from newapp.forms import ImageForm
from newapp.models import  Image,Student,Admission,Marks
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def emailSend(request):
    if request.method == 'POST':
       message = request.POST['message']
       email = request.POST['email']
       name = request.POST['name']
       send_mail(
           name,
           message,
           'settings.EMAIL_HOST_USER',
           [email],
           fail_silently=False
       )
    return render(request,'sendEmail.html')

def student(request):
    if request.method == "POST":
        sname = request.POST.get('name')
        regno = request.POST.get('regno')
        address = request.POST.get('address')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        en=Student(sname=sname,regno=Admission.objects.get(regno=regno),address=address,taluka=taluka,district=district,state=state,pincode=pincode)
        en.save()
        # Student.objects.create(sname=sname,regno=regno,address=address,taluka=taluka,district=district,state=state,pincode=pincode)

    return render(request,"student.html")

def admission(request):
    if request.method == "POST":
        regno = request.POST.get('regno')
        sname = request.POST.get('sname')
        classes = request.POST.get('classes')
        branch = request.POST.get('branch')
        doa = request.POST.get('doa')
        semester = request.POST.get('semester')
        en=Admission(regno=regno,sname=sname,classes=classes,branch=branch,doa=doa,semester=semester)
        en.save()
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #        form.save()
    # form = ImageForm()
        # Admission.objects.create(regno=regno,sname=sname,classes=classes,branch=branch,doa=doa,semester=semester)

    return render(request,"admission.html")

def new(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'newapp/s.html',{'img':img,'form':form})

        

def marks(request):
    dict={}
    if request.method == "POST":
        regno = request.POST.get('regno')
        subject = request.POST.get('subject')
        mark = request.POST.get('mark')
        semester = request.POST.get('semester')
        year = request.POST.get('year')
        en=Marks(regno=Admission.objects.filter(regno=regno).first(),subject=subject,mark=mark,semester=semester,year=year)
        en.save()
        # Marks.objects.all(user=user,regno=regno,subject=subject,mark=mark,semester=semester,year=year)
    
    return render(request,"marks.html")
        
def feedback(request):
    adm = Student.objects.all()
    m = Marks.objects.all()
    a = Admission.objects.all()
    return render(request,"feedback.html",{'data': adm,
                                           'mdata': m,
                                           'adata': a
                                           })
 
def thank(request):
    dict={
    'message':"Congrats you are admited"
    }
    return render(request,"thank.html",dict) 