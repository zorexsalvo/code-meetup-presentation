from django.db import models

# Create your models here.


class Attendee(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField(Attendee)
