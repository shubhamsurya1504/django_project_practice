from django.shortcuts import render

from student.models import Country, City, Student, Company

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class StudentList(ListView):
    model = Student



class StudentListCreate(CreateView):
    model = Student
    fields = ['user', 'student_name', 'city', 'address', 'branch', 'education', 'experience']

    # fields = ['number', 'year', 'inward_number','next_date',
    #                  'action_other',
    #                 'advocate', 'party_names','opposite_party_names',
    #                 'submitted_date','subject',
    #                 'inward_date','receiver_name',
    #                 'notice_subject','document','document1','document2']

    success_url = reverse_lazy('student1_list')
	# success_url = reverse_lazy('books_cbv:book_new')

class StudentListUpdate(UpdateView):
    model = Student
    fields = ['user', 'student_name', 'city', 'address', 'branch', 'education', 'experience']
    success_url = reverse_lazy('student1_list')

     # fields = ['number', 'year', 'inward_number','next_date',
    #                  'action_other',
    #                 'advocate', 'party_names','opposite_party_names',
    #                 'submitted_date','subject',
    #                 'inward_date','receiver_name',
    #                 'notice_subject','document','document1','document2']
    # # fields = ['name']
    # success_url = reverse_lazy('student:student1_list')

class StudentListDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student1_list')

	# fields = ['user', 'student_name', 'city', 'address', 'branch', 'education', 'experience']
    # success_url = reverse_lazy('student:student1_list')





def view_django(request):

    return render(request,'django.html',{})


def view_index(request):

    return render(request,'index.html',{})


def view_ty(request):

    return render(request,'ty.html',{})


def view_sy(request):

    return render(request,'sy.html',{})


def view_fy(request):

    return render(request,'fy.html',{})



def view_hello(request):

    return render(request,'hello.html',{})




def view_hello_20(request):   

    return render(request,'hello-20.html',{})



def view_record(request):

    stud_record = Student.objects.all()
    city_record = City.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'record.html',{'stud12':stud_record,'city12':city_record})


       # return render_to_response('courtcase/report_display.html', {'entry_list': q, 'entry_list1': q1,})


    # return render_to_response('hello.html', {'entry_list': q, 'entry_list1': q1,})





# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# Note that once we’ve done this in all these views, we no longer need to import loader and Ht




# Create your views here.
