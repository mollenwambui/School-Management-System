from django.shortcuts import redirect, render

from Schoolsystem.models import Student
from Schoolsystem.forms import  StudentsForm

# Create your views here.
def studentList(request):
    student=Student.objects.all()
    return render(request,"studentsList.html",{"students":student})

def studentForm(request) :
    if request.method=="POST":

        student=StudentsForm(request.POST,request.FILES)
        if student.is_valid():
            student.save()
            return redirect ("studentsList")
        else:
            print(student.errors)  
    else:
        student=StudentsForm          
    return render(request,"studentsForm.html",{'form':student})


# def teachersForm(request)  :
#     teacher=TeachersForm()  
#     return render(request,"teachersform.html",{'form':teacher})

# def staffsForm(request)   :
#     staffs=StaffsForm() 
#     return render(request,"staffsform.html",{'form':staffs})
    
def home(request):
    return render(request,"home.html")
