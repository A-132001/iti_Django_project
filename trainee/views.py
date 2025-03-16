from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Trainee 
from track.models import Track
from .decorators import require_auth
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views import View
# @require_auth
# def TraineeList(req):
#     context = {}
#     # context["all_trainees"] = Trainee.objects.all()
#     context["all_trainees"] = Trainee.objects.filter(isactive=True)
#     return render(req,"trainee/showtrainees.html",context)

########## Class Based View way
@method_decorator(require_auth, name='dispatch')
class TraineeListView(View):
    template_name = "trainee/showtrainees.html"
    def get(self,req):
        context = {
            "all_trainees": Trainee.objects.filter(isactive=True)
        }
        return render(req, self.template_name, context)
        
# @require_auth
# def AddTrainee(req):
#     if(req.method == "POST"):
#         Trainee.objects.create(name=req.POST["trname"],
#                                email=req.POST["tremail"],
#                                image=req.FILES["trimage"],
#                                )
#     return render(req,"trainee/addtrainee.html")

########## Class Based View way
@method_decorator(require_auth, name='dispatch')
class AddTraineeView(View):
    template_name = "trainee/addtrainee.html"
    def get(self,req):
        return render(req,self.template_name)
    def post(self,req):
        Trainee.objects.create(name=req.POST["trname"],
                               email=req.POST["tremail"],
                               image=req.FILES["trimage"],
                               track=Track.objects.get(id=1),
                               )
        return render(req,self.template_name)
        
# @require_auth
# def UpdateTrainee(req,id):
#     trainee = Trainee.objects.get(id=id)
#     context = {"trainee":trainee}
#     if(req.method == "POST"):
#         Trainee.objects.filter(id=id).update(name=req.POST["trname"],
#                                email=req.POST["tremail"],
#                                image=req.FILES["trimage"],)
#         return redirect('trainee_list')
#     return render(req, 'trainee/updatetrainee.html',context)

# def DeleteTrainee(req,id):
#     trainee = Trainee.objects.get(id=id)
#     trainee.isactive=False
#     trainee.save()
#     return redirect("trainee_list")

####### Update and delete using generic based view

@method_decorator(require_auth, name='dispatch')
class UpdateTraineeView(UpdateView):
    model = Trainee
    template_name = "trainee/updatetrainee.html"
    context_object_name = "trainee"
    
    def get(self,request,pk):
        trainee = Trainee.objects.get(id=pk)
        return render(request, 'trainee/updatetrainee.html',{"trainee":trainee})
        
    def post(self, request,pk):
        trainee = self.get_object()

        trainee.name = request.POST.get("trname", trainee.name)
        trainee.email = request.POST.get("tremail", trainee.email)

        if "trimage" in request.FILES:
            trainee.image = request.FILES["trimage"]

        trainee.save()
        return redirect('trainee_list')

    def get_success_url(self):
        return reverse_lazy('trainee_list') 
    
    
@method_decorator(require_auth, name='dispatch')
class DeleteTraineeView(View):
    def get(self, request, id):
        trainee = Trainee.objects.get(id=id)
        trainee.isactive = False
        trainee.save()
        return redirect("trainee_list")
        
