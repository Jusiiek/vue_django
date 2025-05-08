from rest_framework import serializers

class AuthTokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
