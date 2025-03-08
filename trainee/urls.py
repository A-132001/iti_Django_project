from django.urls import path
from .views import *

urlpatterns = [
    path('', Home ,name="home"),
    path('showtrainees/', TraineeList , name='trainee_list'),
    path('addtrainee/',AddTrainee,name="addtrainee"),
]