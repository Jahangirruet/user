from django.shortcuts import render
from django.shortcuts import render
from django.conf import ENVIRONMENT_VARIABLE
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request, user)
            messages.info(request,'user logged in')
            return render(request, 'login.html')    
        else :
            messages.info(request,'user not found')
            return render(request, 'login.html')
    else:
        return  render(request, 'login.html')



