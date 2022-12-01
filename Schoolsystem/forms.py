from django import forms

from Schoolsystem.models import Student

class StudentsForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"


# STREAM_CHOICES=(("AdaLab","AdaLab"),("AnitaB","AnitaB"),("HopperLab","HopperLab"))
# GENDER_CHOICES=(("Male","Male"),("Female","Female"),("prefer not to say","prefer not to say"))
# class StudentsForm(forms.Form):
#     first_name=forms.CharField(label="Enter first name" ,max_length=15,widget=forms.TextInput(attrs={'placeholder':'first name'}))  
#     last_name=forms.CharField(label="Enter last name" ,max_length=15,widget=forms.TextInput(attrs={'placeholder':'last name'}))
#     email=forms.EmailField(label="Enter email" ,max_length=30,widget=forms.TextInput(attrs={'placeholder':'email'}))
#     gender=forms.ChoiceField(choices=GENDER_CHOICES,    label="Enter your Gender")
#     address=forms.CharField(label="Enter you address",widget=forms.TextInput(attrs={'placeholder':'address'}))
#     streams = forms.ChoiceField(choices = STREAM_CHOICES,label="Enter your stream")
#     # stream=forms.CharField(max_length=10,label="Enter your stream",widget=forms.TextInput(attrs={'placeholder':'stream'}))
#     age=forms.IntegerField(label="Enter you age",widget=forms.TextInput(attrs={'placeholder':'age'}))
#     admission_number=forms.IntegerField(label="Enter your admission number",widget=forms.TextInput(attrs={'placeholder':'admission number'}))
#     phone_number=forms.IntegerField(label="Enter phone number",widget=forms.TextInput(attrs={'placeholder':'phone number'}))
#     emergency_contact=forms.IntegerField(label="Enter your emergency contact",widget=forms.TextInput(attrs={'placeholder':'emergency contact'}))
#     profile=forms.ImageField


# UNIT_CHOICES=(("Python","Python"),("Kotlin","Kotlin"),("frontend web","Frontend web"),("IOT","Internet Of Things"),("User Research","User Research"),("UI/UX Design","UI/UX Design"),("Proffessional Development","Proffessional Development"),("Navigate Your Journey","Navigate Your Journey")) 

# class TeachersForm(forms.Form):
#     first_name=forms.CharField(label="Enter first name",max_length=15,widget=forms.TextInput(attrs={'placeholder':'first name'}))
#     last_name=forms.CharField(label="Enter first name",max_length=15,widget=forms.TextInput(attrs={'placeholder':'last name'}))
#     unit_choices=forms.ChoiceField(label="Enter the units you are expert in",choices=UNIT_CHOICES)
#     email=forms.EmailField(label="Enter email",max_length=30,widget=forms.TextInput(attrs={'placeholder':'email'}))
#     contacts=forms.IntegerField(label="Enter contact",widget=forms.TextInput(attrs={'placeholder':'contact'}))

# OCCUPATION_CHOICES=(("Chef","Chef"),("Cook","Cook"),("Matron","Matron"),("Garderner","Gardener"),("GateKeeper","GateKeeper"),("Accountant","Accountant"),("Lead","CodeHive Lead"),("Event","Event Planner"),("Nurse","Nurse")) 
# class StaffsForm(forms.Form):
#      first_name=forms.CharField(label="Enter first name",max_length=15,widget=forms.TextInput(attrs={'placeholder':'first name'}))
#      last_name=forms.CharField(label="Enter first name",max_length=15,widget=forms.TextInput(attrs={'placeholder':'last name'}))
#      Occupation_specialty=forms.ChoiceField(label="Enter your occupational specialty ",choices=OCCUPATION_CHOICES)
#      email=forms.EmailField(label="Enter email",max_length=30,widget=forms.TextInput(attrs={'placeholder':'email'}))
#      contacts=forms.IntegerField(label="Enter contact",widget=forms.TextInput(attrs={'placeholder':'contact'}))




