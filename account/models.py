from django.db import models

# Create your models here.
class Locations(models.Model):
    loc_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.loc_name

class Programs(models.Model):
    loc_name=models.ForeignKey(Locations,on_delete=models.CASCADE)
    prgm_name=models.CharField(max_length=250)
    def __str__(self):
        return self.prgm_name

class Courses(models.Model):
    loc_name=models.ForeignKey(Locations,on_delete=models.SET_NULL,blank=True,null=True)
    prgm_name=models.ForeignKey(Programs,on_delete=models.SET_NULL,blank=True,null=True)
    course_name=models.CharField(max_length=250)
    def __str__(self):
        return self.course_name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)

class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    duration=models.IntegerField()
    fee=models.IntegerField()

    def _str_(self) :
        return self.name

class Staff(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=15)
    phno=models.CharField(max_length=10)
    def __str__(self):
        return self.name
