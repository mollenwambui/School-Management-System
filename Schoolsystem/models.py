from distutils.command.upload import upload
import email
from email.policy import default
from turtle import mode
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=20,null=True)
    school_address=models.TextField(null=True)
    school_email=models.EmailField(max_length=20,null=True)
    location=models.CharField(null=True,max_length=20)
    contact=models.IntegerField(null=True)


class Student(models.Model)  :
    first_name=models.CharField(max_length=15,null=True)  
    last_name=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=30,null=True)
    GENDER_CHOICES=(("Male","Male"),("Female","Female"),("Prefer not to  say","Prefer not to say"))
    gender=models.CharField(max_length=18,null=True,choices=GENDER_CHOICES)
    address=models.TextField(null=True)
    country = models.CountryField(blank_label='(select country)',null=True)
    STREAM_CHOICES=(("AdaLab","AdaLab"),("AnitaB","AnitaB"),("HopperLab","HopperLab"))
    stream=models.CharField(max_length=10,null=True,choices=STREAM_CHOICES)
    age=models.PositiveSmallIntegerField(null=True)
    admission_number=models.IntegerField(null=True)
    School=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name='Student_School')
    phone_number=models.IntegerField(null=True)
    emergency_contact=models.IntegerField(null=True)
    profile=models.ImageField

class StudentId(models.Model) :
    student=models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name='StudentId_Student') 
    date_issued=models.DateField(default=timezone.now)
    expiry_date=models.DateField(default=timezone.now)
    profile_picture=models.ImageField

class TeachersPanel(models.Model):
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=15,null=True)  
    UNIT_CHOICES=(("Python","Python"),("Kotlin","Kotlin"),("frontend web","Frontend web"),("IOT","Internet Of Things"),("User Research","User Research"),("UI/UX Design","UI/UX Design"),("Proffessional Development","Proffessional Development"),("Navigate Your Journey","Navigate Your Journey")) 
    unit_specialty= models.CharField(max_length=25,null=True,choices=UNIT_CHOICES)   
    contacts=models.IntegerField(null=True)
    email=models.EmailField(max_length=30,null=True)
    profile=models.ImageField
    school=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name='TeachersPanel_School')


class SchoolFees(models.Model)   :
    student= models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name='SchoolFees_Student')
    full_fees=models.IntegerField(null=True)
    amount_paid=models.IntegerField(null=True)
    balance=models.IntegerField(null=True)
    receipt=models.ForeignKey('Receipt',null=True,on_delete=models.CASCADE,related_name='SchoolFees_Receipt')

class Receipt(models.Model) :
    student= models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name='Receipt_Student')
    school_account=models.ForeignKey('SchoolAccount',null=True,on_delete=models.CASCADE,related_name='Receipt_SchoolAccount')
    amount_paid=models.IntegerField(null=True)
    balance=models.IntegerField(null=True)
    receipt_number=models.IntegerField(null=True)

class SchoolAccount(models.Model) :
    School=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name='SchoolAccount_School')
    account_name=models.CharField(max_length=25,null=True)
    account_number=models.IntegerField(null=True)

class Staff(models.Model):
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=15,null=True)  
    OCCUPATION_CHOICES=(("Chef","Chef"),("Cook","Cook"),("Matron","Matron"),("Garderner","Gardener"),("GateKeeper","GateKeeper"),("Accountant","Accountant"),("Lead","CodeHive Lead"),("Event","Event Planner"),("Nurse","Nurse")) 
    Occupation_specialty= models.CharField(max_length=15,null=True,choices=OCCUPATION_CHOICES)   
    contacts=models.IntegerField(null=True)
    email=models.EmailField(max_length=30,null=True)
    profile=models.ImageField
    school=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name='Staff_School')


class AcademicAnalysis(models.Model):
    student= models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name='AcademicAnalysis_Student')
    GRADE_CHOICES= (("A","A"),("B","B+"),("B","B"),("B","B-"),("C","C+"),("C","C"),("C","C-"),("D","D"),("E","E")) 
    grade=models.CharField(max_length=15,null=True,choices=GRADE_CHOICES)

    
class LibraryManagement(models.Model)  :
    student= models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name='LibraryManagement_Student')
    date_issued=models.DateTimeField(default=timezone.now)
    return_date=models.DateTimeField(default=timezone.now)













