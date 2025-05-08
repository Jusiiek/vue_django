from rest_framework import serializers

from .models import AuthToken

class AuthTokenResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthToken
        fields = ('token')
