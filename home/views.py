from django.shortcuts import render,redirect
from django.views import View
from account.models import Staff,Contact
from .forms import StudentForm
from .models import Student,Coursesadd
from django.contrib import messages

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'loginhome.html')
from django.shortcuts import render,redirect

class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'loginenquiry.html',{'form':customer})

class Staffs(View):
    def get(self,request):
        staff=Staff.objects.all()
        return render(request,'loginstaff.html',{'form':staff})

class StudEdit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Student.objects.filter(stud_id=edit1)
        course=Coursesadd.objects.all()
        return render(request,'logineditform.html',{'forms':edit,"course":course})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method=='POST':
            if Student.objects.filter(stud_id=edit1).exists():
                if request.POST['stud_address']:
                    Student.objects.filter(stud_id=edit1).update(stud_address=request.POST['stud_address'])
                if request.POST['stud_place']:
                    Student.objects.filter(stud_id=edit1).update(stud_place=request.POST['stud_place'])
                if request.POST['stud_name']:
                    Student.objects.filter(stud_id=edit1).update(stud_name=request.POST['stud_name'])
                if request.POST['course_name']:
                    Student.objects.filter(stud_id=edit1).update(course_name=request.POST['course_name'])
                if request.POST['stud_email']:
                    Student.objects.filter(stud_id=edit1).update(stud_email=request.POST['stud_email'])
                if request.POST['stud_phone']:
                    Student.objects.filter(stud_id=edit1).update(stud_phone=request.POST['stud_phone'])
              
                students=Student.objects.all()
                return render(request,'showstudents.html',{'form':students})

class StudDelete(View):
    def get(self,request):
        delete=request.GET['delete']
        Student.objects.filter(stud_id=delete).delete()
        students=Student.objects.all()
        return render(request,'showstudents.html',{'form':students})

class Profile(View): 
    def get(self,request):
        if request.session['email'] is not None:
            customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'loginprofile.html',{'customer':customer})

class Editprofile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render(request,'editprofile.html',{'customer':edit})
    def post(self,request):
        edit1=request.session['email']
        if request.method=="POST":
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Staff.objects.filter(email=request.POST['email']).exists():
                        edit=Staff.objects.filter(email=edit1)
                        messages.error(request,"email id already exists")
                        return render(request,"editprofile.html",{'customer':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Staff.objects.filter(email=request.session['email'])
                return render(request,'loginprofile.html',{'customer':customer})


class StudentAdd(View):
    def get(self,request): 
        form = StudentForm()
        return render(request,'addstudent.html',{'forms':form})
    def post(self,request):
        if request.method=="POST":
            form=StudentForm(request.POST)
            if form.is_valid():
               form.save()
               students=Student.objects.all()
               return render(request,'showstudents.html',{'form':students})
            else:
                print("form not valid")
            return redirect("showstudents")

class Showstudents(View):
    def get(self,request):
        student=Student.objects.all()
        return render(request,'showstudents.html',{'form':student})


        

