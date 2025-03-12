from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def Login(req):
    if req.method == "POST" and "loginbtn" in req.POST:
        username = req.POST['username']
        password = req.POST["password"]
        user = authenticate(req,username=username,password=password)
        # print(user)
        if user != None:
            login(req,user)
            return redirect("trainee_list")
        else:
            context={'error':'error'}
            return render(req,'account/login_page.html',context)
    return render(req,'account/login_page.html')



def Logout(req):
    logout(req)
    return redirect("login_url")
def Register(req):
    if req.method == 'POST' and 'registerbtn' in req.POST:
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        repeat_password = req.POST['repeat_password']
        
        if not username or not password or not email:
            return render(req,'account/register.html',{'error':"you can't send username,password or email empty"})
        
        if password != repeat_password:
            return render(req,'account/register.html',{'error':"password doesn't equal repeated password"})
        if User.objects.filter(username=username).exists():
            return render(req,'account/register.html',{'error':"This User name already exist"})
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        login(req,user)
        return redirect("trainee_list")
    return render(req,'account/register.html')