from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USER NAME ALREADY TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email ALREADY TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                            password=password)
                user.save();
                return redirect('login')
                print("USER CREATED...")
        else:
            messages.info(request,"PASSWORD DOES NOT MATCH...")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'INVALID CREDENTIALS TO LOGIN')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
