from django.shortcuts import render
from django.http  import HttpResponse

def Home(req):
    return HttpResponse("<h1>Hello from Trainee page</h1")

def TraineeList(req):
    return render(req,"trainee/showtrainees.html")

def AddTrainee(req):
    return render(req,"trainee/addtrainee.html")

def UpdateTrainee(req):
    return render(req,"trainee/updatetrainee.html")

def DeleteTrainee(req):
    return render(req,"trainee/deletetrainee.html")