from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        """
        allows to define crucial aspects like associated models, which fields to include and any other things
        """
        model=User
        fields="__all__"
    """def create(self,validated_data):
        ""
        yo create method le chai it creates and return a new Attendance instance,
        given the validated data.
        ""
        return User.objects.create(**validated_data)
        ""yesle chai it creates a new User object using create() method of the User model's manager('objects') ani "**validated_data" le chai validated_data dictionary lai keyword argument ma change garcha that means each key value pair chai as an argument pass huncha create() menthod ma so that tyo method can accpt any numberb of fields defined in user model and set their calues according to the provided data
        ""
"""