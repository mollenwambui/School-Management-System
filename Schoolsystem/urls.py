# from importlib.resources import path
from django.urls import path
from . import views


urlpatterns = [
    path("studentsList/",views.studentList,name="studentsList"),
    path("studentsform/",views.studentForm,name="studentForm"),
]
