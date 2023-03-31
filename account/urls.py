from django.urls import path
from .import views

urlpatterns = [
    path('',views.mainhome,name="mainhome"),
    path('aboutorg/',views.aboutorg,name="aboutorg"),
    path('aboutrec/',views.aboutrec,name="aboutrec"),
    path('aboutlead/',views.aboutlead,name="aboutlead"),
    path('aboutexam/',views.aboutexam,name="aboutexam"),
    path('maingallery/',views.maingallery,name="maingallery"),
    path('course/',views.course,name="course"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('forgot/',views.forgotpswd,name="forgot"),
    
]
