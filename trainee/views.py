from django.shortcuts import render
from django.http  import HttpResponse
from .models import Trainee 

def TraineeList(req):
    context = {}
    context["all_trainees"] = Trainee.objects.all()
    return render(req,"trainee/showtrainees.html",context)

def AddTrainee(req):
    return render(req,"trainee/addtrainee.html")

def UpdateTrainee(req,id):
    return render(req,"trainee/updatetrainee.html")

def DeleteTrainee(req,id):
    return render(req,"trainee/deletetrainee.html")