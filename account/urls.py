from django.urls import path
from .views import *
urlpatterns = [
    path('login/',Login ,name='login_url'),
    path('logout',Logout,name='logout_url'),
    path('register',Register,name='register_url'),
]
