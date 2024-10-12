from django.db import models


# model for the student record

class student(models.Model):

    student_name=models.CharField(max_length=200)
    student_age=models.PositiveIntegerField()
    student_email=models.EmailField(unique=True)
    student_address=models.TextField()
    student_mobile_number=models.TextField()


    def __str__(self):
        return self.student_name

