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

def modified(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("Teacher:view_teachers")
        else:
            context = {
                "form": form
            }
            return render(request, "teachers/edit_teacher.html", context)
            

    else:
        form = TeacherForm(instance=teacher)
    context = {
        "form": form,
        "teacher": teacher,
    }
    return render(request, "teachers/edit_teacher.html", context)


def edit_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    print("get method")
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        print("inside Post")
        if form.is_valid():
            firstName = form.cleaned_data["firstName"]
            print(firstName)
            lastName = form.cleaned_data["lastName"]
            qualifications = form.cleaned_data["qualifications"]
            email = form.cleaned_data["email"]
            form.save()
            return redirect("Teacher:view_teachers")
        else:
            print(form.errors)

    else:
        print("else block")
        print(request.method)
        form = TeacherForm(instance=teacher)
    context = {
        "form": form,
    }
    return render(request, "teachers/edit_teacher.html", context)

"""
def edit_teacher(request, id):
    function for admin to edit teacher information
    teacher = get_object_or_404(Teacher, pk=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('Teacher:view_teachers')
        else: 
            form = form
            print(form.errors)
            return render(request, 'teachers/edit_teacher.html', {'form': form})
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/edit_teacher.html', {'form': form, 'teacher':teacher})
"""
    
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    teacher.delete()
    return redirect('Teacher:view_teachers')

def create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Teacher:view_teachers')
        else:
            print(form.errors)
            return redirect('Teacher:view_teachers')
    else:
        form = TeacherForm()
    return render(request, 'teachers/add_teacher.html', {'form': form})
        

