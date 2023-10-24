from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student
from .forms import StudentForm

# Create your views here.

def view_students(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, 'students/view_students.html', context)


def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('view_students')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
        return render(request, 'students/add_student.html', {'form': form})
