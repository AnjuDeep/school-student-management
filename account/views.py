from django.shortcuts import redirect,render
from .models import Staff,Course,Contact
from django.contrib import messages


def mainhome(request): 
    return render(request,"mainhome.html")

def aboutorg(request):
    return render(request,"about1.html")
def aboutrec(request):
    return render(request,"about2.html")
def aboutlead(request):
    return render(request,"about3.html")
def aboutexam(request):
    return render(request,"about4.html")

def maingallery(request):
    return render(request,"maingallery.html")
def login(request):
    if request.method=="POST":
      email=request.POST['email']
      password=request.POST['password']
      try:
        check_user=Staff.objects.get(email=email,password=password)
        request.session['email']=check_user.email
        request.session['name']=check_user.name
        request.session['phno']=check_user.phno
        return redirect('loginhome')
      except Staff.DoesNotExist:
        messages.error(request,'Invalid username or password')
        return redirect('login')
    return render(request,'login.html')
    
def signup(request):
    if request.method=="POST":
        name=request.POST["name"] 
        email=request.POST["email"] 
        password1=request.POST["password1"] 
        phno=request.POST["phno"] 
        password2=request.POST["password2"]
        if password1 == password2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email already exist')
                return redirect('signup')
            else:
                customer = Staff.objects.create(email=email,name=name,password=password1,phno=phno)
                customer.save()
                messages.info(request, 'user created')
            return redirect('login')
        else:
            messages.info(request,"password is not match")
            return redirect("signup")
    else:
      return render(request,'signup.html')

def course(request):
     courses={
    'course':Course.objects.all()
    }
     return render(request,'maincourse.html',courses)

def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phone=request.POST['phone'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'maincontact.html',dicts)
    return render(request,'maincontact.html')

def forgotpswd(request):
  if request.method=="POST":
    email=request.POST['email']
    password=request.POST['password1']
    if Staff.objects.filter(email=email).exists():
      Staff.objects.filter(email=email).update(password=password)
      return redirect("login")
    else:

      messages.error(request,"Invalid Email id")
      return redirect('forgot')
  return render(request,'forgotpswd.html')
    
 