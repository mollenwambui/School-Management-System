from logging import PlaceHolder
from django import forms


class StudentsForm(forms.Form):
    first_name=forms.CharField(label="Enter first name" ,max_length=15,widget=forms.TextInput(attrs={'placeholder':'first name'}))  
    last_name=forms.CharField(label="Enter last name" ,max_length=15,widget=forms.TextInput(attrs={'placeholder':'last name'}))
    email=forms.EmailField(label="Enter email" ,max_length=30,widget=forms.TextInput(attrs={'placeholder':'email'}))
    # GENDER_CHOICES=(("Male","Male"),("Female","Female"))
    gender=forms.CharField(label="Gender",widget=forms.TextInput(attrs={'placeholder':'gender'}))
    address=forms.CharField(label="Enter you address",widget=forms.TextInput(attrs={'placeholder':'address'}))
    STREAM_CHOICES=(("AdaLab","AdaLab"),("AnitaB","AnitaB"),("HopperLab","HopperLab"))
    stream=forms.CharField(max_length=10,label="Enter your stream",widget=forms.TextInput(attrs={'placeholder':'stream'}))
    age=forms.IntegerField(label="Enter you age",widget=forms.TextInput(attrs={'placeholder':'age'}))
    admission_number=forms.IntegerField(label="Enter your admission number",widget=forms.TextInput(attrs={'placeholder':'admission number'}))
    phone_number=forms.IntegerField(label="Enter phone number",widget=forms.TextInput(attrs={'placeholder':'phone number'}))
    emergency_contact=forms.IntegerField(label="Enter your emergency contact",widget=forms.TextInput(attrs={'placeholder':'emergency contact'}))
    profile=forms.ImageField
