from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Course
from .decorators import require_auth

@require_auth
def CourseList(req):
    # all_courses = Course.objects.all()
    all_courses = Course.objects.filter(isactive=True)
    context={"courses":all_courses}
    return render(req,'course/courselist.html',context)

@require_auth
def AddCourse(req):
    if req.method == "POST":
        Course.objects.create(name=req.POST["crname"],
                              instructor=req.POST["crinstructor"],
                              description=req.POST["crdescription"])
    return render(req,'course/addcourse.html')

@require_auth
def UpdateCourse(req,id):
    course = Course.objects.get(id=id)
    context = {'course':course}
    if req.method == "POST":
        Course.objects.filter(id=id).update(name=req.POST["crname"],
                              instructor=req.POST["crinstructor"],
                              description=req.POST["crdescription"])
        return redirect("course_list")
    return render(req,'course/updatecourse.html',context)

def DeleteCourse(req,id):
    course = Course.objects.get(id=id)
    course.isactive = False
    course.save()
    return redirect("course_list")