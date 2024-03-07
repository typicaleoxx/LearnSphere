from django.db import models
from course_management.models import Course
# Create your models here.
class Task(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    description=models.TextField()
    deadline=models.DateTimeField()
    status=models.CharField(max_length=250)