from django.urls import path
from .views import *

urlpatterns = [
    path('', TraineeListView.as_view() , name='trainee_list'),
    path('addtrainee/',AddTraineeView.as_view(),name="add_trainee"),
    path('updatetrainee/<pk>',UpdateTraineeView.as_view(),name="update_trainee"),
    path('deletetrainee/<int:id>',DeleteTraineeView.as_view(),name="delete_trainee"),
    
]