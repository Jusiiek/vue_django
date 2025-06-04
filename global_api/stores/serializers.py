import docker
from rest_framework import serializers
from .models import Store

client = docker.from_env()


class StoreSerializer(serializers.ModelSerializer):
    api_state = serializers.SerializerMethodField()
    web_state = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = (
            'domain',
            'state',
        )

    def _get_state_with_suffix(self, obj, suffix):
        domain = obj.domain
        container_name = f"{domain}_{suffix}"
        try:
            container = client.containers.get(container_name)
            status = container.status
        except docker.errors.NotFound:
            status = 'not found'
        except Exception:
            status = "crashed"

        return status

    def get_api_state(self, obj):
        return self._get_state_with_suffix(obj, suffix="api")

    def get_web_state(self, obj):
        return self._get_state_with_suffix(obj, suffix="web")
