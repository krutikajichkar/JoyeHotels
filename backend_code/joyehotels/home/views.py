from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_page(request):

    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username=username)

            if not user_obj.exists():
                # messages.add_message(request, messages.INFO, "Change Username")
                messages.warning(request, "Account not found")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username = username , password = password)
            if not user_obj:
                messages.warning(request, "invalid password!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            login(request, user_obj)
            return redirect('/')
           
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            # messages.add_message(request, messages.INFO, "Change Username")
            messages.warning(request, "Username already exits!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request, 'register.html')

def hotels(request):
     return render(request, 'hotels.html')

def contact(request):
     return render(request, 'contact.html')

