from django.urls import path
from .views import *
from .api.views import *
urlpatterns = [
    path('',Tracklist,name='track_list'),
    path('addtrack/',AddTrack,name='add_track'),
    path('updatetrack/<int:id>',UpdateTrack,name='update_track'),
    path('deletetrack/<int:id>',DeleteTrack,name='delete_track'),
    #API
    path('api/<int:id>',Get_Update_Delete,name='update_track_api')
    
]
