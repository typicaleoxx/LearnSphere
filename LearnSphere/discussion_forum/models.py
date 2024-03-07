from django.db import models
from authentication.models import User
from course_management.models import Course


# Create your models here.
class Discussion(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField()
