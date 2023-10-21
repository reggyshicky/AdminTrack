from django.shortcuts import render
from .models import Student

# Create your views here.
def homepage(request):
    return render(request, 'home/homepage.html', {
        
    })

def view_student(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, 'students/student.html', context)


    
