from django.db import models

YEAR_CHOICES = [
    (1, 'First Year'),
    (2, 'Second Year'),
    (3, 'Third Year'),
	(4, 'Fourth Year'),
]
# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    yearOfStudy = models.IntegerField(choices=YEAR_CHOICES)
    
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
