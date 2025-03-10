from django.shortcuts import render
from django.http  import HttpResponse
from .models import Trainee 

def TraineeList(req):
    all_trainee = Trainee.objects.all()
    print(all_trainee)
    return render(req,"trainee/showtrainees.html")

def AddTrainee(req):
    return render(req,"trainee/addtrainee.html")

def UpdateTrainee(req):
    return render(req,"trainee/updatetrainee.html")

def DeleteTrainee(req):
    return render(req,"trainee/deletetrainee.html")