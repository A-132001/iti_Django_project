from django.shortcuts import render
from django.http  import HttpResponse

def Home(req):
    return HttpResponse("<h1>Hello from course</h1")

def CourseList(req):
    
    return render(req,'course/courselist.html')

def AddCourse(req):
    return render(req,'course/addcourse.html')

def UpdateCourse(req,id):
    return render(req,'course/courselist.html')

def DeleteCourse(req):
    return render(req,'course/courselist.html')


def Login(req):
    return render(req,'course/login.html')

def Logout(req):
    return HttpResponse("<h1>Hello from Logout Page</h1")

def Register(req):
    return HttpResponse("<h1>Hello from Registeration Page</h1")