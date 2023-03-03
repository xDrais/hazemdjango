from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from .forms import LoginForm


def signIn(req):
    form = LoginForm()
    if req.method == 'GET':
        return render(req,'users/form.html',{'form':form})
    if req.method == 'POST':
        username = req.POST['username']
        pwd = req.POST['password']
        user = authenticate(req,username=username,password=pwd)
        if user is not None:
            login(request=req,user=user)
            return redirect( 'listeventview' )
        else:
            return render(req,'users/form.html',{'error':'credentials invalid'})