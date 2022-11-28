from django.shortcuts import render ,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method =="POST":
    #     chech if  a user exists
    #     with the username and password
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request, 'First_page.html')
        else:
            return render (request,'home.html', {'error': "Invalid Login Credentials."})   
    else:
        return render(request,'home.html')         


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['ConfirmPassword']:
            # both the password matched
            # now check if previous user exits
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                return redirect(home)
        else:
            return render(request, 'register.html', {'error': "Password Don't Match"})
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect(home)





