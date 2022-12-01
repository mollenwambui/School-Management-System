# from importlib.resources import path
from django.urls import path
from . import views


urlpatterns = [
    path("studentsList/",views.studentList,name="studentsList"),
    path("studentsform/",views.studentForm,name="studentForm"),
    # path("teachersform/",views.teachersForm,name="teachersForm"),
    # path("staffsform/",views.staffsForm,name="staffsform")
    path("home/",views.home,name="home")
]
