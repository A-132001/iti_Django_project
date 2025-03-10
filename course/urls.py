from django.urls import path
from .views import *

urlpatterns = [
    path('',CourseList,name="course_list"),
    path('addcourse/',AddCourse,name="addcourse"),
    path('updatecourse/<int:id>',UpdateCourse,name="addcourse"),
    path('deletecourse/',DeleteCourse,name="deletecourse"),
    path('login/',Login,name="login"),
    path('logout/',Logout,name="logout"),
    path('register/',Register,name="register"), 
]