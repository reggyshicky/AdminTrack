from django.db import models

QUALIFICATION_CHOICES = [
    ('doctrate', 'Doctrate'),
    ('masters', 'Masters'),
    ('degree', 'Degree'),
    ('diploma', 'Diploma'),
    ('certificate', 'Certificate'),
]
# Create your models here.
class Teacher(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES, null=True, blank=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'