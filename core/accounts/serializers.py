from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "password")