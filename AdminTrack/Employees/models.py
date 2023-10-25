from django.db import models

# Create your models here.

JOB_ROLES = [
    ('librarian', 'Librarian'),
    ('counselor', 'Guidance Counselor'),
    ('nurse', 'School Nurse'),
    ('coach', 'Coach'), 
]

class Employee(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    jobRole = models.CharField(max_length = 50, choices=JOB_ROLES)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.jobRole}"