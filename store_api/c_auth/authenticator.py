from rest_framework.authentication import BaseAuthentication
from .utils import get_authenticated_user


class BearerTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return get_authenticated_user(request)
