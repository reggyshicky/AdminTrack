from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def view_employees(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    return render(request, 'employees/view_employees.html', context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_employees')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def edit_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('view_employees')
    else:
        form = EmployeeForm(instance=employee)
        
    return render(request, 'employees/edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('view_employees')
    