from django.db import models

# Create your models here.
class Coursesadd(models.Model):
    course_name=models.CharField(max_length=200)
    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    stud_id=models.AutoField(primary_key=True)
    stud_name=models.CharField(max_length=30)
    stud_phone=models.CharField(max_length=10)
    stud_email=models.EmailField(max_length=100)
    course_name = models.ForeignKey(Coursesadd,default=1,on_delete=models.CASCADE)
    stud_address=models.CharField(max_length=100)
    stud_place=models.CharField(max_length=100)
    
    