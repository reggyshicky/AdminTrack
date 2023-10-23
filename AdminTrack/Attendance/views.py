from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from .forms import AttendanceForm
from django.contrib import messages
# Create your views here.

def list_attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/list_attendance.html', {'attendance_records': attendance_records})


def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_attendance')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/create_attendance.html', {'form': form})

def update_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('list_attendance')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance/update_attendance.html', {'form': form, 'attendance': attendance})  

def list_attendance_by_status(request):
    status = request.GET.get('status', '')
    if status:
        attendance_records = Attendance.objects.filter(attendanceStatus=status)
    else:
        attendance_records = Attendance.objects.all()
    return render(request, 'attendance/list_attendance_by_status.html', {'attendance_records': attendance_records,'status': status})
        

def delete_attendance_record(request, attendance_id):
    if request.method == 'POST':
        attendance_record = Attendance.objects.get(pk=attendance_id)
        attendance_record.delete()
        messages.success(request, 'Attendance record deleted successfully.')
        return redirect('list_attendance')
    return render(request, 'attendance/list_attendance.html')