from django.db import models
from authentication.models import User
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=250)
    instructor=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()
    duration=models.IntegerField()

class Enrollment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    date_enrolled=models.DateTimeField