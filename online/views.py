from django.contrib import messages, auth
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.urls import reverse
from online.models import UserRegistration


def home(request):
    return render(request ,'home.html')

def register(request):
   if request.method == 'POST':
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       phone = request.POST['ph']
       psw   = request.POST['psw']
       psw1 = request.POST['psw-repeat']

       if UserRegistration.objects.filter(email = email).exists() :
           print("Email id already Exists")
           messages.info(request, "This Email id already exists")
           return redirect('register')

       elif UserRegistration.objects.filter(phone = phone).exists():
           messages.info(request, "Phone No already exists")
           return redirect('register')

       elif psw1!=psw :
           messages.info(request, "Password Mismatch!!")
           return redirect('register')

       else :

           online_user = UserRegistration.objects.create(first_name = fname, last_name = lname , email = email , phone = phone )
           online_user.set_password(psw)
           online_user.save()

           print("User Created")

           return redirect('register')

   else:
     return render(request, 'register.html')



def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        phone = request.POST['ph']
        psw = request.POST['psw']

        user = UserRegistration.objects.filter(phone = phone).first()
        user = authenticate(request, phone = phone, password = psw )

        if user is not None :
            auth.login(request, user)
            return HttpResponseRedirect((reverse('main')))

        else :
            messages.info(request, "Invalid Phone Number or Password")

            return HttpResponseRedirect(reverse('login'))

    else :
           return render(request, 'login.html')



def Logout(request):
    logout(request)
    return HttpResponseRedirect((reverse('main')))

def cart(request):
    return render(request, 'cart.html')