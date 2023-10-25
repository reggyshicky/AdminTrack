from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["student", "dateOfAttendance", "attendanceStatus"]
        
        widgets = {
            'dateOfAttendance': forms.DateInput(attrs={'type': 'date'}),
        }
        
        