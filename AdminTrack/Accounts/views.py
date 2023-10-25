from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistrationForm

# Create your views here.

def homepage(request):
    return render(request, 'home/homepage.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request,'contacts.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('admin_dashboard')
                
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, f'Invalid Credentials')
            return redirect("admin_login")
        
    return render(request, 'admin_login.html')


    
def admin_logout(request):
    auth.logout(request)
    return redirect('homepage')
    
