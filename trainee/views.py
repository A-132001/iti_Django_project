from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Trainee 
from .decorators import require_auth

from django.views import View
@require_auth
def TraineeList(req):
    context = {}
    # context["all_trainees"] = Trainee.objects.all()
    context["all_trainees"] = Trainee.objects.filter(isactive=True)
    return render(req,"trainee/showtrainees.html",context)

@require_auth
def AddTrainee(req):
    if(req.method == "POST"):
        Trainee.objects.create(name=req.POST["trname"],
                               email=req.POST["tremail"],
                               image=req.FILES["trimage"],
                               )
    return render(req,"trainee/addtrainee.html")

@require_auth
def UpdateTrainee(req,id):
    trainee = Trainee.objects.get(id=id)
    context = {"trainee":trainee}
    if(req.method == "POST"):
        Trainee.objects.filter(id=id).update(name=req.POST["trname"],
                               email=req.POST["tremail"],
                               image=req.FILES["trimage"],)
        return redirect('trainee_list')
    return render(req, 'trainee/updatetrainee.html',context)
def DeleteTrainee(req,id):
    trainee = Trainee.objects.get(id=id)
    trainee.isactive=False
    trainee.save()
    return redirect("trainee_list")