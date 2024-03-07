from django.db import models
from authentication.models import User
# Create your models here.
class Streak(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    last_active_date=models.DateTimeField()
    streak_count=models.CharField(max_length=250)
