from rest_framework import serializers

from .models import UserDetails


class UserDetailsSerializer(serializers.ModelSerializer):
    """Serializer for the User Details Object"""

    class Meta:
        model = UserDetails
        fields = ["user", "first_name", "surname", "dob", "gender", "image"]
