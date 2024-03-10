from rest_framework import serializers
from .models import Discussion

class DiscussionSerializer(serializers.Serializer):
    class Meta:
        model=Discussion
        fields="__all__"
