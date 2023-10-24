from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request,'contacts.html')
    
def admin_login(request):
    return render(request, 'admin_login.html')

def homepage(request):
    return render(request, 'home/homepage.html', {
        
    })