from django.urls import path
from .views import *

urlpatterns = [
    path('',CourseList,name="course_list"),
    path('addcourse/',AddCourse,name="add_course"),
    path('updatecourse/<int:id>',UpdateCourse,name="update_course"),
    path('deletecourse/<int:id>',DeleteCourse,name="delete_course"),
]