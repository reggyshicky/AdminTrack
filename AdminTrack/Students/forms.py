from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["firstName", "lastName", "dateOfBirth", "yearOfStudy"]
        
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }
