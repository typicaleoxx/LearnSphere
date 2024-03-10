from rest_framework import serializers
from .models import Course, Enrollment


class CourseSerializer(serializers.Serializer):
    class Meta:
        """class meta chai hamile serialise garna chaine models, ani fields haru tyo define garna use garcham
        in short it tell how the serialiser should behave
        """
        model = Course
        fields = "__all__"
    def create(self, validated_data):
        return Course.create(validated_data)

class EnrollmentSerializer(serializers.Serializer):
    class Meta:
        model=Enrollment
        fields="__all__"
    def create(self,validated_data):
        return Enrollment.objects.create(**validated_data)