from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from .models import Teacher
from .forms import TeacherForm

# Create your views here.

def view_teachers(request):
    """Function to allow admin view list of teachers"""
    teachers = Teacher.objects.all()
    context = {
        "teachers": teachers,
    }
    return render(request, 'teachers/view_teachers.html', context)

def edit_teacher(request, id):
    """function for admin to edit teacher information"""
    teacher = get_object_or_404(Teacher, pk=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('view_teachers')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/edit_teacher.html', {'form': form, 'teacher':teacher})
    
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    teacher.delete()
    return redirect('view_teachers')

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_teachers')
    else:
        form = TeacherForm()
        return render(request, 'teachers/add_teacher.html', {'form': form})
