from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.Serializer):
    class Meta:
        model=Attendance
        fields="__all__"
        """
        #indicating that all fields frm Attendance model to be included in the serializer
        """
    """def create(self,validated_data):
        create method takes validated data(data that has passed validation based on the serializer's field definitions. It represents validated data that can be safely used to create a new object in the database.
        ,it is auto provided by drf during serialization)
        return Attendance.objects.create(**validated_data)
"""