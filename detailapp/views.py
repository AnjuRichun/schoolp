from urllib import request

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from detailapp.forms import StudentForm
from detailapp.models import Department, Course, Student
from django.http import JsonResponse


# Create your views here.
def detail(request,id):
    try:
        detail = Department.objects.get(id=id)
    except Exception as e:
        raise e
    return render(request, 'department.html', {'detail': detail})


def new(request):

    return render(request,"new.html")


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentForm
   # messages.info(request,"order confirmed")
    success_url = reverse_lazy('detailapp:addnew')


   # StudentForm.request_change = True
   # form = StudentForm()
   # if request.method == 'POST':
    #    form = StudentForm(request.POST)
    #    if form.is_valid():
      #      form.save()
       #     messages.info(request, "order confirmed")
       # return redirect('detailapp:addnew')
    #return render(request,'student_form.html',{'form':form})

def load_course(request):
    department_id=request.GET.get("department")
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'course_add.html', {'courses': courses})

def addnew(request):
    return render(request,"addnew.html")






