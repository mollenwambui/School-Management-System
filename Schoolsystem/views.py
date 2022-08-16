from django.shortcuts import render

from Schoolsystem.models import Student
from Schoolsystem.forms import StudentsForm

# Create your views here.
def studentList(request):
    student=Student.objects.all()
    return render(request,"studentsList.html",{"students":student})

def studentForm(request) :
    student=StudentsForm()
    return render(request,"studentsForm.html",{'form':student})
    

