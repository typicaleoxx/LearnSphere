"""from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)
initially we had done this and by that approach we did not classify role as we have different user roles which is instructor and students so we are following the approach below
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True)
    ROLE_CHOICES = (
        ("mentor", "Mentor"),
        ("student", "Student"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    """
    AbstractUser chai its an inbuild model in django, which already includes username, email and password
    so if we wanted to create our own user model, we started using AbstractUser as our base so that we didnt have to define username, email password again.
    along with that hamro project anusar we wanted extra fields which is role,so we provided choices for that field 
    """
