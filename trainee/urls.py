from django.urls import path
from .views import *

urlpatterns = [
    path('', TraineeList , name='trainee_list'),
    path('addtrainee/',AddTrainee,name="add_trainee"),
    path('updatetrainee/',UpdateTrainee,name="update_trainee"),
    path('deletetrainee/',DeleteTrainee,name="delete_trainee"),
    
]