from django import forms
from .models import Student
from account.models import Course

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        labels={
            'stud_name' :"Student Name",
            'stud_phone' : "Phone Number",
            'stud_email' : "Email ID",
            'course_name':"Course Name",
            'stud_address' :"Address",
            'stud_place' :"Place"
                }