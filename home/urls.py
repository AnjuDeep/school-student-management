from django.urls import path
from .import views

urlpatterns = [
    path('loginhome/',views.Home.as_view(),name="loginhome"), 
    path('enquiry/',views.Enquiry.as_view(),name="enquiry"),
    path('staff/',views.Staffs.as_view(),name="staff"),
    path('studentadd/',views.StudentAdd.as_view(),name="studentadd"),
    path('showstudents/',views.Showstudents.as_view(),name="showstudents"),
    path('edit/',views.StudEdit.as_view(),name="edit"),
    path('delete/',views.StudDelete.as_view(),name="delete"),
    path('profile/',views.Profile.as_view(),name="profile"),
    path('editprofile/',views.Editprofile.as_view(),name="editprofile"),
      
]
