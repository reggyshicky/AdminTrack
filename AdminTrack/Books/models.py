from django.db import models

AVAILABILITY_CHOICES = [
    ('available', 'Available'),
    ('checked_out', 'Checked Out'),
    ('reserved', 'Reserved'),
    ('lost', 'Lost'),
    ('damaged', 'Damaged'),
]
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author_first_name = models.CharField(max_length=50)
    author_last_name = models.CharField(max_length=50)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    availabilityStatus = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author_first_name} {self.author_last_name}'