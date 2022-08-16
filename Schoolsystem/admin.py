from django.contrib import admin

from Schoolsystem.models import AcademicAnalysis, LibraryManagement, Receipt, School, SchoolAccount, SchoolFees, Staff, Student, StudentId, TeachersPanel

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(TeachersPanel)
admin.site.register(SchoolFees)
admin.site.register(Receipt)
admin.site.register(SchoolAccount)
admin.site.register(Staff)
admin.site.register(AcademicAnalysis)
admin.site.register(LibraryManagement)
