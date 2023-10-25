from django.db import models
from Students.models import Student


# Create your models here.
ATTENDANCE_CHOICES = [
    ('Present', 'Present'),
    ('Absent', 'Absent'),
]
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendanceStatus = models.CharField(max_length=30, choices=ATTENDANCE_CHOICES)
    dateOfAttendance = models.DateField()
     
    def __str__(self):
        return f"{self.student.firstName} - {self.attendanceStatus}"