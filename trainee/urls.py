from django.urls import path
from .views import *

urlpatterns = [
    path('',viewname,name="home")
]