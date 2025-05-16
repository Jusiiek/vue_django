from rest_framework import serializers
from .models import User

from django.utils.timesince import timesince
from django.utils.timezone import now


class UserSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'is_staff',
            'is_active',
            'is_superuser',
            'is_global_user',
            'created'
        )

    def get_created(self, obj):
        return f"{timesince(obj.date_joined, now())} ago"
