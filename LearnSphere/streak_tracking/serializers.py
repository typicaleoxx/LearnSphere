from rest_framework import serializers
from .models import Streak

class StreakSerializer(serializers.Serializer):
    class Meta:
        model=Streak
        fields="__all__"